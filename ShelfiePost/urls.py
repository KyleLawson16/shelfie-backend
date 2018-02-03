from django.conf.urls import url
from ShelfiePost.views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='PostListAPIView'),
    url(r'^(?P<random_post_id>[\w-]+)/$', PostDetailAPIView.as_view(), name='PostDetailAPIView' ),
]
