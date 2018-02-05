from rest_framework import serializers

from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge
from ShelfiePrize.models import Prize
from ShelfieUser.models import User

class GameUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_game_id'

class GameChallengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = [
            'point_value',
            'random_challenge_id',
            'name',
            'description',
        ]

class GamePrizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = [
            'name',
            'description',
        ]

class GameFansSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'random_user_id',
        ]

class GameSerializer(serializers.HyperlinkedModelSerializer):
    url = GameUrlField(view_name='ShelfieGame:GameDetailAPIView')
    challenges = GameChallengesSerializer(many=True)
    prizes = GamePrizesSerializer(many=True)

    fans = serializers.SerializerMethodField()

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
            'prizes',
            'fans',
        ]

    def get_fans(self, obj):
        return obj.fans.count()
