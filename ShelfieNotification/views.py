# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from django.shortcuts import get_object_or_404, redirect, render

from ShelfieNotification.serializers import NotificationListSerializer
from ShelfieNotification.filters import NotificationFilter
from ShelfieNotification.models import Notification

from rest_framework import filters, generics, mixins
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from knox.auth import TokenAuthentication

# Create your views here.
class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationListSerializer
    queryset = Notification.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []
    filter_class = NotificationFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user', 'game', 'challenge')

    def get_queryset(self):
        notifications = Notification.objects.all().order_by('-timestamp')
        return notifications
