from django.conf.urls import url
from ShelfieGame.views import GameListAPIView, GameDetailAPIView, GameLeaderboardAPIView

urlpatterns = [
    url(r'^$', GameListAPIView.as_view(), name='GameListAPIView'),
    url(r'^(?P<random_game_id>[\w-]+)/$', GameDetailAPIView.as_view(), name='GameDetailAPIView' ),
    url(r'^(?P<random_game_id>[\w-]+)/leaderboard/$', GameLeaderboardAPIView.as_view(), name='GameLeaderboardAPIView' ),
]
