from rest_framework import serializers

from ShelfieNotification.models import Notification
from ShelfieUser.models import User

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'actor',
            'recipient',
            'post',
            'category',
            'message',
            'active',
        ]

class NotificationActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'random_user_id',
            'username',
            'profile_picture',
        ]

class NotificationListSerializer(serializers.ModelSerializer):
    actor = NotificationActorSerializer()

    class Meta:
        model = Notification
        fields = [
            'actor',
            'recipient',
            'post',
            'category',
            'message',
            'active',
            'timestamp',
        ]
