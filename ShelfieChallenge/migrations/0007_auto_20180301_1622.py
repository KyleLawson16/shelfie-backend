# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-02 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieChallenge', '0006_auto_20180301_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='background_photo',
            field=models.ImageField(default='https://s3-us-west-1.amazonaws.com/shelfie-challenge/challenges/grey_and_black_photo.png', upload_to='challenges'),
        ),
    ]