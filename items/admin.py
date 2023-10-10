from django.contrib import admin

# Register your models here.
from .models import Category, Item


@admin.register(Category)
class FontAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('name__startswith',)
    fields = ('name',)


@admin.register(Item)
class FontAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('category', )
    search_fields = ('name__startswith',)
    fields = ('name', 'category', 'description', 'icon', 'script')
