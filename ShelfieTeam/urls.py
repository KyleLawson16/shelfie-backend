from django.conf.urls import url
from ShelfieTeam.views import TeamListAPIView, TeamDetailAPIView

urlpatterns = [
    url(r'^$', TeamListAPIView.as_view(), name='TeamListAPIView'),
    url(r'^/(?P<random_team_id>[\w-]+)$', TeamDetailAPIView.as_view(), name='TeamDetailAPIView' )
]
