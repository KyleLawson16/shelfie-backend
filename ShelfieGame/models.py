# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

from ShelfieChallenge.models import Challenge
from ShelfiePrize.models import Prize
from ShelfieUser.models import User
from ShelfieTeam.models import Team

def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id


class Game(models.Model):
    random_game_id = models.CharField(
        'Random Game Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    date = models.DateTimeField(
        editable=True,
    )
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='home_team',
        blank=True,
        null=True,
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='away_team',
        blank=True,
        null=True,
    )
    organization = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='organization',
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    challenges = models.ManyToManyField(
        Challenge
    )
    prizes = models.ManyToManyField(
        Prize,
        blank=True,
    )
    fans = models.ManyToManyField(
        User,
        blank=True,
    )

    def __unicode__(self):
        return str(self.home_team) + '-' + str(self.away_team) + '-' + str(self.date)
