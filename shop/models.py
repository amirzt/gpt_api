from django.db import models

from user.models import CustomUser


class ZarinpalCode(models.Model):
    code = models.CharField(max_length=255, null=False, blank=False)
    package_name = models.CharField(max_length=255, null=False, default='')
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GooglePlayCode(models.Model):
    code = models.CharField(max_length=255, null=False, blank=False)
    package_name = models.CharField(max_length=255, null=False, default='')
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppStoreCode(models.Model):
    code = models.CharField(max_length=255, null=False, blank=False)
    package_name = models.CharField(max_length=255, null=False, default='')
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ZarinPalPlan(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    is_available = models.BooleanField(default=True)
    duration = models.IntegerField(null=False, blank=False)
    is_special = models.BooleanField(default=False)
    package_name = models.CharField(max_length=255, null=False, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GooglePlayPlan(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    is_available = models.BooleanField(default=True)
    duration = models.IntegerField(null=False, blank=False)
    google_play_code = models.CharField(max_length=255, null=True)
    package_name = models.CharField(max_length=255, null=False, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppStorePlan(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    is_available = models.BooleanField(default=True)
    duration = models.IntegerField(null=False, blank=False)
    app_store_code = models.CharField(max_length=255, null=True)
    package_name = models.CharField(max_length=255, null=False, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    class GatewayChoices(models.TextChoices):
        ZARINPAL = 'zarinpal'
        GOOGLEPLAY = 'googleplay'
        APPSTORE = 'appstore'

    class StateChoices(models.TextChoices):
        PENDING = 'pending'
        SUCCESS = 'success'
        FAILED = 'failed'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, null=True)
    price = models.FloatField(null=False, blank=False)
    gateway = models.CharField(max_length=255, choices=GatewayChoices.choices)
    gateway_code = models.CharField(max_length=255, null=True)
    tracking_code = models.CharField(max_length=255, null=True)
    duration = models.IntegerField(default=0)
    state = models.CharField(max_length=255, choices=StateChoices.choices, default=StateChoices.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GoogleAdmob(models.Model):
    class Types(models.TextChoices):
        BANNER = 'banner'
        NATIVE = 'native'
        INTERSTITIAL = 'interstitial'
        REWARDED = 'rewarded'

    code = models.CharField(max_length=255, null=False, blank=False)
    package_name = models.CharField(max_length=255, null=False, default='')
    type = models.CharField(max_length=255, choices=Types.choices)

