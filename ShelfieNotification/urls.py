from django.conf.urls import url
from ShelfieNotification.views import (
    NotificationListAPIView,
    notification_update_api,
)

urlpatterns = [
    url(r'^$', NotificationListAPIView.as_view(),
        name='NotificationListAPIView'),
    url(r'^/read$', notification_update_api,
        name='notification_update_api'),
]
