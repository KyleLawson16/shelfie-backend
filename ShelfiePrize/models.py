# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

from ShelfieUser.models import User

def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id


class Prize(models.Model):
    random_prize_id = models.CharField(
        'Random Prize Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    name = models.CharField(
        max_length=120,
    )
    description = models.CharField(
        max_length=120,
    )
    winner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    background_photo = models.ImageField(
        upload_to='prizes',
        default='prizes/shelfie_prize_background.png'
    )

    def __unicode__(self):
        return str(self.name)
