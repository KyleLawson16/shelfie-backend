# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

from ShelfieUser.models import User
from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge

# Create your models here.
def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id


class Post(models.Model):
    random_post_id = models.CharField(
        'Random Post Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )
    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE
    )
    is_video = models.BooleanField(
        default=False,
    )
    media_url = models.CharField(
        max_length=120,
    )
    caption = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )
    likes = models.ManyToManyField(
        User,
        related_name='likes',
        blank=True,
    )

    def __unicode__(self):
        return str(self.user) + '-' + str(self.game) + '-' + str(self.challenge)


class Report(models.Model):
    random_report_id = models.CharField(
        'Random Report Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    message = models.CharField(
        max_length=120,
        blank=True,
        null=True,
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __unicode__(self):
        return str(self.random_report_id)
