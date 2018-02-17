from __future__ import unicode_literals

import re

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _



def random_id():
    unique_id = get_random_string(
        length=12, allowed_chars='0123456789')
    return unique_id


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser,
                     first_name, last_name, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, first_name, last_name,
                    **extra_fields):
        if len(first_name) > 1:
            first_name = first_name[0].upper() + first_name[1:]
        if len(last_name) > 1:
            last_name = last_name[0].upper() + last_name[1:]

        return self._create_user(username, email, password, False, False, first_name, last_name, **extra_fields)

    def create_superuser(self, username, email, password, first_name, last_name):
        user = self._create_user(
            username, email, password, True, True, first_name, last_name)
        user.is_active = True
        user.save(using=self._db)
        return user



GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        db_index=True,
        verbose_name='Username',
        unique=True,
        max_length=255,
        help_text=_(
            'Required. 255 characters or fewer. Letters, numbers and \
            @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a valid username.'),
                _('invalid')
            )
        ]
    )
    random_user_id = models.CharField(
        'Random User Id',
        editable=False,
        unique=True,
        max_length=120,
        default=random_id,
        primary_key=True

    )
    email = models.EmailField(
        db_index=True,
        verbose_name='Email',
        unique=True,
        max_length=255
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=60
    )
    middle_name = models.CharField(
        verbose_name='Middle Name',
        max_length=60,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=60
    )
    phone_number = models.CharField(
        blank=True,
        verbose_name='Phone Number',
        max_length=60,
    )
    is_active = models.BooleanField(
        verbose_name='Active User',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff User',
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name='Updated At',
        auto_now=True
    )
    gender = models.CharField(
        'Gender',
        max_length=120,
        choices=GENDER,
        blank=True,
        default="",
    )
    profile_picture = models.CharField(
        max_length=120,
        default="https://shelfie-challenge.s3.amazonaws.com/users%2Fprofile-photos%2Fdefault_profile.png"
    )
    following = models.ManyToManyField(
        "self",
        related_name='following_field',
        blank=True,
        symmetrical=False,
    )
    followers = models.ManyToManyField(
        "self",
        related_name='followers_field',
        blank=True,
        symmetrical=False,
    )




    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __unicode__(self):
        return smart_text(self.first_name + ' ' + self.last_name)

    def get_full_name(self):
        middle_name = ''
        suffix = ''
        if self.middle_name is not None:
            middle_name = ' ' + str(self.middle_name)
        full_name = '%s%s %s' % (
            self.first_name, middle_name, self.last_name)
        return full_name.rstrip()

    def get_short_name(self):
        short_name = '%s %s' % (self.first_name, self.last_name)
        return short_name.rstrip()
