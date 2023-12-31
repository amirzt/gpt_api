# Generated by Django 4.0.6 on 2023-10-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_apikey'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('package_name', models.CharField(max_length=100)),
                ('is_force', models.BooleanField(default=False)),
            ],
        ),
    ]
