from rest_framework import serializers

from ShelfieNotification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'actor',
            'recipient',
            'category',
            'message',
        ]
