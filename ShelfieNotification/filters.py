import django_filters
from ShelfieNotification.models import Notification
from ShelfieNotification.serializers import NotificationSerializer
from rest_framework import generics

class NotificationFilter(django_filters.FilterSet):
    class Meta:
        model = Notification
        fields = ['recipient', 'post']
