# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfiePrize', '0002_auto_20180215_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='description',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='prize',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
