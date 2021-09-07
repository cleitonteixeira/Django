from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Users, Farms, Seasons
from .serializers import UsersSerializer, FarmsSerializer, SeasonsSerializer


class  UsersAPIView(APIView):
    """
    API DE USUARIOS 3UP
    """
    def get( self, request ):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    
    def post( selfe, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Sucesso":"Usuário Criado com Sucesso!"}, status=status.HTTP_201_CREATED)


class FarmsAPIView(APIView):
    """
    API DE FAZENDAS
    """
    def get( self, request ):
        farms = Farms.objects.all()
        serializer = FarmsSerializer(farms, many=True)
        return Response(serializer.data)
    
    def post( selfe, request):
        serializer = FarmsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Sucesso":"Fazenda Criada com Sucesso!"}, status=status.HTTP_201_CREATED)


class SeasonsAPIView(APIView):
    """
    API DE ESTAÇÕES
    """
    def get( self, request ):
        season = Seasons.objects.all()
        serializer = SeasonsSerializer(season, many=True)
        return Response(serializer.data)
    
    def post( selfe, request):
        serializer = SeasonsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Sucesso":"Estação Criada com Sucesso!"}, status=status.HTTP_201_CREATED)