# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-14 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieChallenge', '0010_challenge_background_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='background_photo',
            field=models.ImageField(default='challenges/shelfie_challenge_background.png', upload_to='challenges'),
        ),
    ]