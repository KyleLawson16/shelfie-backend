from rest_framework import serializers

from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge
from ShelfiePrize.models import Prize
from ShelfieUser.models import User
from ShelfiePost.models import Post
from ShelfieTeam.models import Team

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
            'background_photo',
        ]

class GamePrizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = [
            'name',
            'description',
            'background_photo',
        ]

class GameFansSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'fans_ids',
        ]

class GameTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'random_team_id',
            'name',
            'location',
            'logo_url',
        ]

class GameSerializer(serializers.HyperlinkedModelSerializer):
    url = GameUrlField(view_name='ShelfieGame:GameDetailAPIView')
    challenges = GameChallengesSerializer(many=True)
    prizes = GamePrizesSerializer(many=True)
    home_team = GameTeamSerializer()
    away_team = GameTeamSerializer()
    organization = GameTeamSerializer()

    fans_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Game.objects.all(),
        source='fans'
    )

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
            'fans_ids',
        ]


class GameLeaderboardSerializer(serializers.ModelSerializer):
    leaderboard = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = [
            'leaderboard',
        ]

    def get_leaderboard(self, obj):
        posts = Post.objects.filter(game=obj)
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
            followers = []
            for follower in user.followers.all():
                followers.append(follower.random_user_id)
            for post in user_posts:
                user_points += post.challenge.point_value
            leaderboard_object = {
                'random_user_id': user.random_user_id,
                'username': user.username,
                'points': user_points,
                'followers': followers,
                'profile_picture': user.profile_picture,
            }
            leaderboard.append(leaderboard_object)
            sorted_leaderboard = sorted(leaderboard, key=lambda k: k['points'], reverse=True)

        print sorted_leaderboard
        return sorted_leaderboard
