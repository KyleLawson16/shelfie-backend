from rest_framework import serializers

from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge

class GameUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_game_id'

class GameChallengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = [
            'point_value',
            'name',
            'description',
        ]

class GameSerializer(serializers.HyperlinkedModelSerializer):
    url = GameUrlField(view_name='ShelfieGame:GameDetailAPIView')
    challenges = GameChallengesSerializer(many=True)

    class Meta:
        model = Game
        fields = [
            'url',
            'random_game_id',
            'date',
            'home_team',
            'away_team',
            'organization',
            'location',
            'challenges',
        ]
