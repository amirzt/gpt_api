from rest_framework import serializers

from shop.models import GooglePlayCode, AppStoreCode, ZarinPalPlan, GooglePlayPlan, AppStorePlan, Transaction, \
    GoogleAdmob


class GooglePlayCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GooglePlayCode
        fields = '__all__'


class AppStoreCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStoreCode
        fields = '__all__'


class ZarinPalPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZarinPalPlan
        fields = '__all__'


class GooglePlayPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GooglePlayPlan
        fields = '__all__'


class AppStorePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStorePlan
        fields = '__all__'


class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = []

    def save(self, **kwargs):
        transaction = Transaction(user=self.context['user'],
                                  price=self.context['price'],
                                  gateway=self.context['gateway'],
                                  gateway_code=self.context['gateway_code'],
                                  duration=self.context['duration'],
                                  description=self.context['description'])
        transaction.save()
        return transaction


class GoogleAdmobSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleAdmob
        fields = '__all__'



