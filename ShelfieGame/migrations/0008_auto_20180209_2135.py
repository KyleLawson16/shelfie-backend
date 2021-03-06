# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfieGame', '0007_auto_20180209_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='ShelfieTeam.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='ShelfieTeam.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='ShelfieTeam.Team'),
        ),
    ]
