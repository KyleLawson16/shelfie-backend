# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShelfieGame', '0003_auto_20180204_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='fans',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
