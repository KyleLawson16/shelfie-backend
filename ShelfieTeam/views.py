import django_filters

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from ShelfieTeam.serializers import TeamSerializer
from ShelfieTeam.models import Team

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, generics, mixins
from knox.auth import TokenAuthentication



class TeamListAPIView(generics.ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    authentication_classes = []
    permission_classes = []
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'location')

    def get_queryset(self):
        return Team.objects.all()

class TeamDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    authentication_classes = []
    permission_classes = []

    def get_object(self, *args, **kwargs):
        random_team_id = self.kwargs.pop('random_team_id')
        team = get_object_or_404(Team, random_team_id=random_team_id)
        return team
