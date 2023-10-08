from django.contrib import admin

# Register your models here.
from support.models import Instagram, EmailAddress, Telegram


@admin.register(Instagram)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('url',)
    fields = ('url',)


@admin.register(EmailAddress)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('email',)
    fields = ('email',)


@admin.register(Telegram)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('url',)
    fields = ('url',)
