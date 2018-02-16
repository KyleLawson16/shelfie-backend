from django.conf.urls import url
from ShelfieUser.views import (
    LoggedInUserAPIView,
    UserCreateAPIView,
    UserDetailAPIView,
    UserListAPIView,
    follow_create_api,
    follow_delete_api,
    validate_user_data
)

urlpatterns = [
    url(r'^users$', UserListAPIView.as_view(),
        name='UserListAPIView'),
    url(r'^users/(?P<random_user_id>[\w-]+)$', UserDetailAPIView.as_view(),
        name='UserDetailAPIView'),
    url(r'^users/follow/add$', follow_create_api,
        name='follow_create_api'),
    url(r'^users/follow/delete$', follow_delete_api,
        name='follow_delete_api'),
    url(r'^create-user$', UserCreateAPIView.as_view(),
        name='UserCreateAPIView'),
    url(r'^users/logged-in-user$', LoggedInUserAPIView.as_view(),
        name='LoggedInUserAPIView'),
    url(r'^validate/user$', validate_user_data,
        name='validate_user_name'),
]
