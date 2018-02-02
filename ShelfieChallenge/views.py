import django_filters

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from ShelfieChallenge.serializers import ChallengeSerializer
from ShelfieChallenge.models import Challenge

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, generics, mixins
from knox.auth import TokenAuthentication



class ChallengeListAPIView(generics.ListAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description', 'point_value')

    def get_queryset(self):
        return Challenge.objects.all().order_by('-point_value')

class ChallengeDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_object(self, *args, **kwargs):
        random_challenge_id = self.kwargs.pop('random_challenge_id')
        challenge = get_object_or_404(Challenge, random_challenge_id=random_challenge_id)
        return challenge
