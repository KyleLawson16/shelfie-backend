from django.conf.urls import url
from ShelfieGame.views import GameListAPIView, GameDetailAPIView

urlpatterns = [
    url(r'^$', GameListAPIView.as_view(), name='GameListAPIView'),
    url(r'^(?P<random_game_id>[\w-]+)/$', GameDetailAPIView.as_view(), name='GameDetailAPIView' )
]
