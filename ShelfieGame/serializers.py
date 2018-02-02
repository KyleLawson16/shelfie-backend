from rest_framework import serializers

from ShelfieGame.models import Game

class GameUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_game_id'

class GameSerializer(serializers.HyperlinkedModelSerializer):
    url = GameUrlField(view_name='ShelfieGame:GameDetailAPIView')

    class Meta:
        model = Game
        fields = [
            'url',
            'random_game_id',
            'date',
            'team_1',
            'team_2',
            'home_team',
            'organization',
            'location',
            'challenges'
        ]
