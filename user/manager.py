
# from comtypes.automation import _
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    # create user with given number and password
    def create_user(self, device_id, password, **extra_fields):
        if not device_id:
            raise ValueError('اطلاعات دستگاه باید وارد شود')

        user = self.model(device_id=device_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, device_id, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(device_id, password, **extra_fields)
