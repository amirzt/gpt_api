from django.db import models


class Instagram(models.Model):
    url = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.url


class EmailAddress(models.Model):
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.email


class Telegram(models.Model):
    url = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.url
