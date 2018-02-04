import django_filters

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from ShelfiePrize.serializers import PrizeSerializer
from ShelfiePrize.models import Prize

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, generics, mixins
from knox.auth import TokenAuthentication



class PrizeListAPIView(generics.ListAPIView):
    serializer_class = PrizeSerializer
    queryset = Prize.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description')

    def get_queryset(self):
        return Prize.objects.all()

class PrizeDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = PrizeSerializer
    queryset = Prize.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []

    def get_object(self, *args, **kwargs):
        random_prize_id = self.kwargs.pop('random_prize_id')
        prize = get_object_or_404(Prize, random_prize_id=random_prize_id)
        return prize
