# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-14 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieUser', '0006_auto_20180217_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(default='https://shelfie-challenge-production.s3.amazonaws.com/users%2Fprofile-photos%2Fshelfie_profile.png', max_length=120),
        ),
    ]
