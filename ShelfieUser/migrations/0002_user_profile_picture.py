# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
