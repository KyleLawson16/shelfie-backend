# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

from ShelfieChallenge.models import Challenge

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
        blank=True,
        null=True
    )
    team_1 = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    team_2 = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    home_team = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    organization = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    challenges = models.ManyToManyField(Challenge, through='GameChallenge')


class GameChallenge(models.Model):
    game_challenge_id = models.CharField(
        'Game Challenge Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    game = models.ForeignKey(Game)
    challenge = models.ForeignKey(Challenge)
