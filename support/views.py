from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from support.models import Instagram, EmailAddress, Telegram
from support.serializers import InstagramSerializer, EmailAddressSerializer, TelegramSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_instagram(request):
    instagram = Instagram.objects.last()
    return Response(InstagramSerializer(instagram).data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_email(request):
    email = EmailAddress.objects.last()
    return Response(EmailAddressSerializer(email).data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_telegram(request):
    telegram = Telegram.objects.last()
    return Response(TelegramSerializer(telegram).data)
