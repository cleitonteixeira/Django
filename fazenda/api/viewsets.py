from django.db.models.query import QuerySet
from rest_framework import generics, serializers
from rest_framework.generics import get_object_or_404

from ..models import Seasons, Users, Farms
from .serializers import SeasonsSerializer, UsersSerializer, FarmsSerializer


class UsersAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class FarmsAPIView(generics.ListCreateAPIView):
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer


class FarmAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer


class SeasonsAPIView(generics.ListCreateAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer

    def get_queryset(self):
        if self.kwargs.get('farm_pk'):
            return self.queryset.filter(farms_id=self.kwargs.get('farm_pk'))
        return self.queryset.all()

class SeasonAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer

    def get_object(self):
        if self.kwargs.get('farm_pk'):
            return get_object_or_404(self.get_queryset(),pk=self.kwargs.get('season_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('season_pk'))