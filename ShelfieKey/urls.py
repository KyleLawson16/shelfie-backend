from django.conf.urls import url
from ShelfieKey.views import AmazonS3ListAPIView

urlpatterns = [
    url(r'^/amazons3$', AmazonS3ListAPIView.as_view(), name='AmazonS3ListAPIView'),
]
