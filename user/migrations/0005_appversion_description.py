# Generated by Django 4.0.6 on 2023-10-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_appversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='appversion',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
