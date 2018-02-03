import django_filters

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from ShelfieGame.serializers import GameSerializer
from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, generics, mixins
from knox.auth import TokenAuthentication



class GameListAPIView(generics.ListAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('home_team', 'date', 'location',
                     'organization')

    def get_queryset(self):
        games = Game.objects.all()
        return games

    def get_object(self):
        games = Game.objects.all()
        new_games = []
        for game in games:
            challenges = game.challenges.all()
            point_values = []
            for challenge in challenges:
                if challenge.point_value not in point_values:
                    point_values.append(challenge.point_value)
            print point_values
            sorted_challenges = {}
            for value in point_values:
                equal_challenges = challenges.filter(point_value=value)
                sorted_challenges[value] = equal_challenges
            print sorted_challenges
            new_games.append(sorted_challenges)
        return new_games


class GameDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []

    def get_object(self, *args, **kwargs):
        random_game_id = self.kwargs.pop('random_game_id')
        game = get_object_or_404(Game, random_game_id=random_game_id)
        return game
