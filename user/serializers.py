import datetime

from rest_framework import serializers

from user.models import CustomUser, AppVersion, ApiKey


class AddCustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['device_id']

    def save(self, **kwargs):
        user = CustomUser(device_id=self.validated_data['device_id'])
        if 'phone' in kwargs:
            user.phone = kwargs['phone']
        if 'email' in kwargs:
            user.email = kwargs['email']
        user.save()
        return user


class GetUserSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField('get_is_expired')

    @staticmethod
    def get_is_expired(obj):
        if obj.expired_at < datetime.datetime.now():
            return True
        return False

    class Meta:
        model = CustomUser
        fields = '__all__'


class GetAppVersion(serializers.ModelSerializer):

    class Meta:
        model = AppVersion
        fields = '__all__'


class GetApiKeysSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiKey
        fields = '__all__'


