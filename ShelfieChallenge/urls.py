from django.conf.urls import url
from ShelfieChallenge.views import ChallengeListAPIView, ChallengeDetailAPIView

urlpatterns = [
    url(r'^$', ChallengeListAPIView.as_view(), name='ChallengeListAPIView'),
    url(r'^(?P<random_challenge_id>[\w-]+)/$', ChallengeDetailAPIView.as_view(), name='ChallengeDetailAPIView' )
]
