# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id


class Team(models.Model):
    random_team_id = models.CharField(
        'Random Team Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    name = models.CharField(
        max_length=120,
    )
    location = models.CharField(
        max_length=120,
        blank=True,
        null=True,
    )
    logo_url = models.ImageField(
        upload_to='teams/logos/',
        null=True,
        blank=True
    )
    point_of_contact = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return str(self.name)
