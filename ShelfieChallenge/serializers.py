from rest_framework import serializers

from ShelfieChallenge.models import Challenge

class ChallengeUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_challenge_id'

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    url = ChallengeUrlField(view_name='ShelfieChallenge:ChallengeDetailAPIView')

    class Meta:
        model = Challenge
        fields = [
            'url',
            'random_challenge_id',
            'name',
            'description',
            'point_value'
        ]
