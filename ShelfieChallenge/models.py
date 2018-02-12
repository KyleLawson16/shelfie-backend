# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id

class Challenge(models.Model):
    random_challenge_id = models.CharField(
        'Random Challenge Id',
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
    point_value = models.IntegerField(
    )

    def __unicode__(self):
        return str(self.name)
