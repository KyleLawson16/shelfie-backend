# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 19:57
from __future__ import unicode_literals

import ShelfieUser.models
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, help_text='Required. 255 characters or fewer. Letters, numbers and             @/./+/-/_ characters', max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='Username')),
                ('random_user_id', models.CharField(default=ShelfieUser.models.random_id, editable=False, max_length=120, primary_key=True, serialize=False, unique=True, verbose_name='Random User Id')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=60, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, max_length=60, verbose_name='Phone Number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active User')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff User')),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='', max_length=120, verbose_name='Gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
