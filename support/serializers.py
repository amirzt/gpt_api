from rest_framework import serializers

from support.models import Instagram, EmailAddress, Telegram


class InstagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instagram
        fields = '__all__'


class EmailAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailAddress
        fields = '__all__'


class TelegramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telegram
        fields = '__all__'
