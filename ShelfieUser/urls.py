from django.conf.urls import url
from ShelfieUser.views import (
    edit_profile_information,
    edit_profile_photo,
    LoggedInUserAPIView,
    UserCreateAPIView,
    UserDetailAPIView,
    UserListAPIView,
    login_redirect,
    validate_user_data
)

urlpatterns = [
    url(r'^profile/$', edit_profile_information,
        name='edit_profile_information'),
    url(r'^profile/change-photo/$', edit_profile_photo,
        name='edit_profile_photo'),
    url(r'^users/$', UserListAPIView.as_view(),
        name='UserListAPIView'),
    url(r'^users/(?P<random_user_id>[\w-]+)/$', UserDetailAPIView.as_view(),
        name='UserDetailAPIView'),
    url(r'^users/create$', UserCreateAPIView.as_view(),
        name='UserCreateAPIView'),
    url(r'^users/logged-in-user$', LoggedInUserAPIView.as_view(),
        name='LoggedInUserAPIView'),
    url(r'^validate/user$', validate_user_data,
        name='validate_user_name'),
]
