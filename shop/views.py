import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from shop.models import ZarinPalPlan, GooglePlayPlan, AppStorePlan, GooglePlayCode, AppStoreCode, ZarinpalCode, \
    Transaction, GoogleAdmob
from shop.serializers import ZarinPalPlanSerializer, GooglePlayPlanSerializer, AppStorePlanSerializer, \
    GooglePlayCodeSerializer, AppStoreCodeSerializer, AddTransactionSerializer, GoogleAdmobSerializer

from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json


import threading

from shop.verifications import update_expire_date
from user.models import CustomUser

ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"

CallbackURL = 'https://addstory.website/api/shop/verify/'


@api_view(['POST'])
@permission_classes([AllowAny])
def get_admob(request):
    admob = GoogleAdmob.objects.filter(package_name=request.data['package_name'])
    serializer = GoogleAdmobSerializer(admob, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_zarinpal_plan(request):
    if 'is_special' in request.data:
        plans = ZarinPalPlan.objects.filter(is_special=True,
                                            package_name=request.data['package_name'],
                                            is_available=True)
    else:
        plans = ZarinPalPlan.objects.filter(is_special=False,
                                            package_name=request.data['package_name'],
                                            is_available=True)
    serializer = ZarinPalPlanSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_googleplay_plan(request):
    plans = GooglePlayPlan.objects.all()
    serializer = GooglePlayPlanSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_appstore_plan(request):
    plans = AppStorePlan.objects.all()
    serializer = AppStorePlanSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_googleplay_code(request):
    codes = GooglePlayCode.objects.all()
    serializer = GooglePlayCodeSerializer(codes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_appstore_code(request):
    codes = AppStoreCode.objects.all()
    serializer = AppStoreCodeSerializer(codes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_zarinpal_url(request):
    plan = ZarinPalPlan.objects.get(id=request.data['plan'])

    serializer = AddTransactionSerializer(data=request.data,
                                          context={'user': request.user,
                                                   'duration': plan.duration,
                                                   'price': plan.price,
                                                   'gateway': 'zarinpal',
                                                   'gateway_code': ZarinpalCode.objects.last().code,
                                                   'description': 'خرید اشتراک ' + plan.title})
    if serializer.is_valid():
        transaction = serializer.save()
        return Response({
            'purchase_url': '?merchant=' + ZarinpalCode.objects.last().code
                            + "&username=" + request.user.username
                            + "&amount=" + str(int(transaction.price))
                            + "&description=" + 'خرید اشتراک ' + plan.title
                            + "&transaction_id=" + str(transaction.id)
        },
            status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def send_request(request):
    req_data = {
        "merchant_id": request.GET['merchant'],
        "amount": int(request.GET['amount']),
        "callback_url": CallbackURL,
        "description": request.GET['description'],
        "metadata": {"username": request.GET['username'], "email": ''},
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']

    transaction = Transaction.objects.get(id=request.GET['transaction_id'])
    transaction.gateway_code = authority
    transaction.save()

    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    # t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']

    if request.GET.get('Status') == 'OK':

        transaction = Transaction.objects.get(gateway_code=t_authority)

        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": ZarinpalCode.objects.last().code,
            "amount": transaction.price,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']

            if t_status == 100:
                # save reservation
                transaction.state = 'success'
                transaction.tracking_code = req.json()['data']['ref_id']
                transaction.save()

                # update expire date
                data = {
                    'user': transaction.user.id,
                    'duration': transaction.duration
                }
                thread = threading.Thread(target=update_expire_date,
                                          args=[data])
                thread.setDaemon(True)
                thread.start()
                #
                context = {
                    'tracking_code': transaction.tracking_code
                }
                return render(request, 'success_payment.html', context)
                # return HttpResponse('Transaction success.\nRefID: ' + str(
                #     req.json()['data']['ref_id']
                # ))
            elif t_status == 101:
                context = {
                    'tracking_code': transaction.tracking_code
                }
                return render(request, 'error_payment.html', context)
                # return HttpResponse('Transaction submitted : ' + str(
                #     req.json()['data']['message']
                # ))
            else:
                return render(request, 'error_payment.html')

                # return HttpResponse('Transaction failed.\nStatus: ' + str(
                #     req.json()['data']['message']
                # ))
        else:
            return render(request, 'error_payment.html')

            # e_code = req.json()['errors']['code']
            # e_message = req.json()['errors']['message']
            # return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return render(request, 'error_payment.html')

        # return HttpResponse('Transaction failed or canceled by user')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bazar_myket_order(request):
    plan = ZarinPalPlan.objects.get(id=request.data['plan'])
    # package_name = CustomUser.objects.get(id=request.user.id).package_name

    serializer = AddTransactionSerializer(data=request.data,
                                          context={'user': request.user,
                                                   # 'package_name': package_name,
                                                   'duration': plan.duration,
                                                   'price': plan.price,
                                                   'gateway': request.data['gateway'],
                                                   'gateway_code': request.data['gateway_code'],
                                                   'description': 'خرید اشتراک ' + plan.title})
    if serializer.is_valid():
        transaction = serializer.save()
        transaction.state = 'success'
        transaction.save()

        user = CustomUser.objects.get(id=request.user.id)
        if user.expire_date < timezone.now():
            user.expire_date = timezone.now() + datetime.timedelta(days=int(plan.duration))
        else:
            user.expire_date += datetime.timedelta(days=int(plan.duration))
        user.save()
        #
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)