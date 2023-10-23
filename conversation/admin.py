from django.contrib import admin

from .models import GPTModel, Conversation, Message


@admin.register(GPTModel)
class FontAdmin(admin.ModelAdmin):
    list_display = ('model_name',)
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('model_name__startswith',)
    fields = ('model_name',)


admin.site.register(Conversation)
admin.site.register(Message)
