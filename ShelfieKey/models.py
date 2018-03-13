# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class AmazonS3(models.Model):
    bucket = models.CharField(
        max_length=120,
    )
    region = models.CharField(
        max_length=120,
    )
    access_key = models.CharField(
        max_length=120,
    )
    secret_access_key = models.CharField(
        max_length=120,
    )
