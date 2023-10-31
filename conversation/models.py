from django.db import models

from user.models import CustomUser


class GPTModel(models.Model):
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name


class Conversation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gpt_model = models.ForeignKey(GPTModel, on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):

    class RoleChoices(models.TextChoices):
        system = 'system', 'system'
        user = 'user', 'user'
        assistant = 'assistant', 'assistant'
        function = 'function', 'function'

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    content = models.TextField(max_length=1000, null=True, blank=False)
    image = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

