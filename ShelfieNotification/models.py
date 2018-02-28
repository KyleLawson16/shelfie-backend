# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models

from ShelfieUser.models import User
from ShelfiePost.models import Post

# Create your models here.
def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id

CATEGORY = (
    ('like', 'Like'),
    ('follow', 'Follow'),
    ('prize', 'Prize'),
)


class Notification(models.Model):
    random_notification_id = models.CharField(
        'Random Notification Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True
    )
    actor = models.ForeignKey(
        User,
        related_name='actor',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        related_name='recipient',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    category = models.CharField(
        max_length=120,
        choices=CATEGORY,
    )
    message = models.CharField(
        max_length=120,
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        default=False,
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __unicode__(self):
        return str(self.random_notification_id)
