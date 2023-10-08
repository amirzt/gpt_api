# Generated by Django 4.0.6 on 2023-10-08 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppStoreCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppStorePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('duration', models.IntegerField()),
                ('app_store_code', models.CharField(max_length=255, null=True)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAdmob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('type', models.CharField(choices=[('banner', 'Banner'), ('native', 'Native'), ('interstitial', 'Interstitial'), ('rewarded', 'Rewarded')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GooglePlayCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GooglePlayPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('duration', models.IntegerField()),
                ('google_play_code', models.CharField(max_length=255, null=True)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZarinpalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZarinPalPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('duration', models.IntegerField()),
                ('is_special', models.BooleanField(default=False)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, null=True)),
                ('price', models.FloatField()),
                ('gateway', models.CharField(choices=[('zarinpal', 'Zarinpal'), ('googleplay', 'Googleplay'), ('appstore', 'Appstore')], max_length=255)),
                ('gateway_code', models.CharField(max_length=255, null=True)),
                ('tracking_code', models.CharField(max_length=255, null=True)),
                ('duration', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
