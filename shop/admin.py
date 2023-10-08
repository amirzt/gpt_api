from django.contrib import admin

# Register your models here.
from shop.models import ZarinpalCode, ZarinPalPlan, GooglePlayCode, GooglePlayPlan, AppStoreCode, AppStorePlan, \
    Transaction, GoogleAdmob


@admin.register(ZarinpalCode)
class FontAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_available')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('code__startswith',)
    fields = ('code', 'is_available', 'package_name')


@admin.register(ZarinPalPlan)
class FontAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'duration', 'is_special')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('title__startswith',)
    fields = ('title', 'price', 'is_available', 'duration', 'description', 'is_special', 'package_name')


@admin.register(GooglePlayCode)
class FontAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_available')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('code__startswith',)
    fields = ('code', 'is_available', 'package_name')


@admin.register(GooglePlayPlan)
class FontAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'duration')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('title__startswith',)
    fields = ('title', 'price', 'is_available', 'duration', 'description', 'google_play_code', 'package_name')


@admin.register(AppStoreCode)
class FontAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_available')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('code__startswith',)
    fields = ('code', 'is_available', 'package_name')


@admin.register(AppStorePlan)
class FontAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'duration')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('title__startswith',)
    fields = ('title', 'price', 'is_available', 'duration', 'description', 'app_store_code', 'package_name')


@admin.register(Transaction)
class FontAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'gateway', 'tracking_code', 'created_at','updated_at')
    list_filter = ('state',)
    search_fields = ('user__startswith',)
    fields = (
        'user', 'description', 'price', 'gateway', 'gateway_code', 'tracking_code', 'duration', 'state',)


@admin.register(GoogleAdmob)
class FontAdmin(admin.ModelAdmin):
    list_display = ('code', 'package_name', 'type')
    # list_filter = ('category', 'is_done', 'date',)
    # search_fields = ('code__startswith',)
    fields = ('code', 'package_name', 'type')