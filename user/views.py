from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from shop.models import Transaction, GoogleAdmob
from shop.serializers import GoogleAdmobSerializer
from user.models import CustomUser, ApiKey, AppVersion
from user.serializers import GetUserSerializer
from rest_framework.authtoken.models import Token
from django.utils import timezone


@api_view(['POST'])
@permission_classes([AllowAny])
def get_user_info(request):
    user = CustomUser.objects.get(device_id=request.data['device_id'])
    serializer = GetUserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def splash(request):
    if request.auth:
        user = CustomUser.objects.get(id=request.user.id)
        if user.expire_date < timezone.now():
            return Response(status=status.HTTP_200_OK, data={'expired': True,
                                                             'username': user.username})
        else:
            return Response(status=status.HTTP_200_OK, data={'expired': False,
                                                             'username': user.username})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        user = CustomUser.objects.get(device_id=request.data['device_id'])
        expired = True if user.expire_date < timezone.now() else False
    except CustomUser.DoesNotExist:

        user = CustomUser(device_id=request.data['device_id'])
        user.save()
        expired = True

    try:
        Transaction.objects.get(user=user,
                                duration=365)
        yearly = True
    except Transaction.DoesNotExist:
        yearly = False

    admob = GoogleAdmob.objects.filter(package_name=request.data['package_name'])
    api_key = ApiKey.objects.get(package_name=request.data['package_name'])

    user.is_active = True
    user.save()
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                     'expired': expired,
                     'yearly': yearly,
                     'username': user.username,
                     'admob': GoogleAdmobSerializer(admob, many=True).data,
                     'api_key': api_key.key
                     })


@api_view(['POST'])
@permission_classes([AllowAny])
def get_app_version(request):
    last_version = AppVersion.objects.filter(package_name=request.data['package_name']).order_by('version').last()
    return Response({'version': last_version.version})
