# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-02 00:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieChallenge', '0008_auto_20180301_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='background_photo',
        ),
    ]