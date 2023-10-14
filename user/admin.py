from django.contrib import admin

from user.models import CustomUser, ApiKey, AppVersion


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'username', 'expire_date')
    list_filter = ('expire_date',)
    search_fields = ('device_id__startswith', 'email__startswith', 'phone__startswith', 'username__startswith',)
    fields = ('device_id', 'username', 'expire_date', 'is_visible', 'is_active', 'is_staff')


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'package_name')
    fields = ('key', 'package_name',)


@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'package_name', 'is_force')
    fields = ('version', 'package_name', 'is_force')
