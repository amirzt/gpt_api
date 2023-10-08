from user.models import CustomUser
from django.utils import timezone
import datetime


def update_expire_date(params):
    user = CustomUser.objects.get(id=params['user'])

    if user.expire_date < timezone.now():
        user.expire_date = timezone.now() + datetime.timedelta(days=int(params['duration']))
    else:
        user.expire_date += datetime.timedelta(days=int(params['duration']))
    user.save()
