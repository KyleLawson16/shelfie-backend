# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieChallenge', '0005_auto_20180301_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='background_photo',
            field=models.ImageField(default='https://shelfie-challenge.s3.amazonaws.com/challenges/grey_and_black_photo.png', upload_to='challenges'),
        ),
    ]