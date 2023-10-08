from datetime import datetime, timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.manager import CustomUserManager
from django.utils.crypto import get_random_string


def get_yesterday():
    return datetime.now() + timedelta(days=-1)


def get_username():
    while True:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        code = get_random_string(length=6, allowed_chars=chars)
        try:
            CustomUser.objects.get(username=code)
        except CustomUser.DoesNotExist:
            break

    return code


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # UUID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    device_id = models.CharField(max_length=255, null=False, unique=True)
    username = models.CharField(max_length=50, unique=True, default=get_username)
    #
    # phone = models.CharField(max_length=11, null=True)
    # email = models.CharField(max_length=255, null=True)
    #
    USERNAME_FIELD = 'device_id'
    REQUIRED_FIELDS = []

    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    expire_date = models.DateTimeField(default=get_yesterday)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
