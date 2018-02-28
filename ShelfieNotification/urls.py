from django.conf.urls import url
from ShelfieNotification.views import (
    NotificationListAPIView
)

urlpatterns = [
    url(r'^$', NotificationListAPIView.as_view(),
        name='NotificationListAPIView'),
]
