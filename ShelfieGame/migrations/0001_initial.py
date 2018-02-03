# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 19:57
from __future__ import unicode_literals

import ShelfieGame.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ShelfieChallenge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('random_game_id', models.CharField(default=ShelfieGame.models.random_id, editable=False, max_length=120, primary_key=True, serialize=False, unique=True, verbose_name='Random Game Id')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('home_team', models.CharField(blank=True, max_length=120, null=True)),
                ('away_team', models.CharField(blank=True, max_length=120, null=True)),
                ('organization', models.CharField(blank=True, max_length=120, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('challenges', models.ManyToManyField(to='ShelfieChallenge.Challenge')),
            ],
        ),
    ]
