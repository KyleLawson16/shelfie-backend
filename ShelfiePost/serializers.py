from rest_framework import serializers

from ShelfiePost.models import Post
from ShelfieUser.models import User
from ShelfieGame.models import Game
from ShelfieChallenge.models import Challenge

class PostUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_post_id'

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'random_user_id',
            'username',
        ]

class PostGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'random_game_id',
        ]

class PostChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = [
            'random_challenge_id',
            'name',
            'point_value',
        ]

class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'random_user_id',
            'username',
        ]

class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = PostUrlField(view_name='ShelfiePost:PostDetailAPIView')
    user = PostUserSerializer()
    game = PostGameSerializer()
    challenge = PostChallengeSerializer()
    likes = PostLikesSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'url',
            'random_post_id',
            'user',
            'game',
            'challenge',
            'is_video',
            'media_url',
            'caption',
            'timestamp',
            'likes',
        ]

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'game',
            'challenge',
            'is_video',
            'media_url',
            'caption',
        ]
