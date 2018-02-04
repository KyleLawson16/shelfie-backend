from rest_framework import serializers

from ShelfiePrize.models import Prize
from ShelfieUser.models import User

class PrizeUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_prize_id'

class PrizeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'random_user_id',
            'username',
        ]

class PrizeSerializer(serializers.HyperlinkedModelSerializer):
    url = PrizeUrlField(view_name='ShelfiePrize:PrizeDetailAPIView')
    user = PrizeUserSerializer()

    class Meta:
        model = Prize
        fields = [
            'url',
            'random_prize_id',
            'name',
            'description',
            'user',
        ]
