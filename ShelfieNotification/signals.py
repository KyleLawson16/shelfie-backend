from ShelfieNotification.models import Notification
from ShelfieNotification.serializers import NotificationSerializer
from ShelfieUser.models import User

from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


def create_like_notification(actor, recipient, post, category, message):
    serializer = NotificationSerializer()
    notification = {
        'actor': actor,
        'recipient': recipient,
        'post': post,
        'category': category,
        'message': message,
        'active': True,
    }

    if not Notification.objects.filter(category=category, actor=actor, recipient=recipient, post=post).exists():
        serializer.create(notification)

    return Response(HTTP_200_OK)

def delete_like_notification(actor, recipient, post, category):
    serializer = NotificationSerializer()

    if Notification.objects.filter(category=category, actor=actor, recipient=recipient, post=post).exists():
        notification = get_object_or_404(Notification, category=category, actor=actor, recipient=recipient, post=post)
        Notification.delete(notification)

    return Response(HTTP_200_OK)

def create_follow_notification(actor, recipient, category, message):
    serializer = NotificationSerializer()
    notification = {
        'actor': actor,
        'recipient': recipient,
        'category': category,
        'message': message,
        'active': True,
    }

    if not Notification.objects.filter(category=category, actor=actor, recipient=recipient).exists():
        serializer.create(notification)

    return Response(HTTP_200_OK)

def delete_follow_notification(actor, recipient, category):
    serializer = NotificationSerializer()

    if Notification.objects.filter(category=category, actor=actor, recipient=recipient).exists():
        notification = get_object_or_404(Notification, category=category, actor=actor, recipient=recipient)
        Notification.delete(notification)

    return Response(HTTP_200_OK)
