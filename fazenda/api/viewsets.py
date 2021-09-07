from rest_framework import generics, serializers

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


class SeasonAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer