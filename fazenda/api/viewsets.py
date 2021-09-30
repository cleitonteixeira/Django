from django.db.models import query
from rest_framework import generics, mixins, serializers
from rest_framework.generics import get_object_or_404
from rest_framework import permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Seasons, Farms, Users
from .serializers import SeasonsSerializer, FarmsSerializer, UsersSerializer

"""
API V1
"""

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

"""
API V2
"""

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer

    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def seasons(self, request, pk=None):
        farm = self.get_object()
        serializer = SeasonsSerializer(farm.season.all(), many=True)
        return Response(serializer.data)

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Seasons.objects.all()

    permission_classes = [IsAuthenticated]

    serializer_class = SeasonsSerializer

class UserAddViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()

    permission_classes = [AllowAny]

    serializer_class = UsersSerializer