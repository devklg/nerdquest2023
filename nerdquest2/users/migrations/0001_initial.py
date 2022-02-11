# Generated by Django 3.2.12 on 2022-02-11 07:19

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('town', models.CharField(blank=True, max_length=100, null=True, verbose_name='town')),
                ('county', models.CharField(blank=True, max_length=100, null=True, verbose_name='County')),
                ('post_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('longitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('lattitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('captcha_score', models.FloatField(default=0.0)),
                ('has_profile', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
