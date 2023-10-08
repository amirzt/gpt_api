from django.contrib import admin

from user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'username', 'expire_date')
    list_filter = ('expire_date',)
    search_fields = ('device_id__startswith', 'email__startswith', 'phone__startswith', 'username__startswith',)
    fields = ('device_id', 'username', 'expire_date', 'is_visible', 'is_active', 'is_staff')

