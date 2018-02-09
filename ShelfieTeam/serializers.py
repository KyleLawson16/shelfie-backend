from rest_framework import serializers

from ShelfieTeam.models import Team

class TeamUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_team_id'

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    url = TeamUrlField(view_name='ShelfieTeam:TeamDetailAPIView')

    class Meta:
        model = Team
        fields = [
            'url',
            'random_team_id',
            'name',
            'location',
            'logo_url',
            'point_of_contact',
        ]
