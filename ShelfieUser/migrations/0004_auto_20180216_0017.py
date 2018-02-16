# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-16 00:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieUser', '0003_auto_20180215_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers_field', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following_field', to=settings.AUTH_USER_MODEL),
        ),
    ]
