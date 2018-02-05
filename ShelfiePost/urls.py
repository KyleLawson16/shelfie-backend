from django.conf.urls import url
from ShelfiePost.views import (
    PostListAPIView,
    PostDetailAPIView,
    PostCreateAPIView,
    like_create_api,
    like_delete_api
)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(),
        name='PostListAPIView'),
    url(r'^create/$', PostCreateAPIView.as_view(),
        name='PostCreateAPIView'),
    url(r'^(?P<random_post_id>[\w-]+)/$', PostDetailAPIView.as_view(),
        name='PostDetailAPIView' ),
    url(r'^(?P<random_post_id>[\w-]+)/like/add/$', like_create_api,
        name='like_create_api'),
    url(r'^(?P<random_post_id>[\w-]+)/like/delete/$', like_delete_api, 
        name='like_delete_api')
]
