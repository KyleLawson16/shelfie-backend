from django.conf.urls import url
from ShelfiePrize.views import PrizeListAPIView, PrizeDetailAPIView

urlpatterns = [
    url(r'^$', PrizeListAPIView.as_view(), name='PrizeListAPIView'),
    url(r'^(?P<random_prize_id>[\w-]+)/$', PrizeDetailAPIView.as_view(), name='PrizeDetailAPIView' )
]
