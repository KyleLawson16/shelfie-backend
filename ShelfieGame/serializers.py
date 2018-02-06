from rest_framework import serializers

from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge
from ShelfiePrize.models import Prize
from ShelfieUser.models import User
from ShelfiePost.models import Post

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

class GameLeaderboardSerializer(serializers.ModelSerializer):
    leaderboard = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = [
            'leaderboard',
        ]

    def get_leaderboard(self, obj):
        posts = Post.objects.all()
        users = []
        for post in posts:
            users.append(post.user)
        filtered_users = []
        for user in users:
            if user not in filtered_users:
                filtered_users.append(user)

        leaderboard = []
        for user in filtered_users:
            leaderboard_object = {}
            user_points = 0
            user_posts = posts.filter(user=user)
            for post in user_posts:
                user_points += post.challenge.point_value
            leaderboard_object = {
                'random_user_id': user.random_user_id,
                'username': user.username,
                'points': user_points
            }
            leaderboard.append(leaderboard_object)

        print leaderboard
        return leaderboard
