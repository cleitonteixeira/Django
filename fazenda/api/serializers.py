from rest_framework import  fields, serializers, status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

from ..models import Farms, Seasons, Users


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = (
            'id',
            'name',
            'latitude',
            'longitude',
            'farms',
            'created',
            'modified'
        )


class FarmsSerializer(serializers.ModelSerializer):
    # Nested Relationship
    seasons = SeasonsSerializer(many=True, read_only=True)

    class Meta:
        model = Farms
        fields = (
            'id',
            'owner',
            'name',
            'cpf',
            'created',
            'modified',
            'seasons'
        )


class UsersSerializer(serializers.ModelSerializer):
    confirm_password = fields.CharField(write_only=True)
    class Meta:
        model = Users
        fields = (
            'id',
            'name',
            'email',
            'username',
            'password',
            'confirm_password',
            'created',
            'modified'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def save(self, **kwargs):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'senha': 'As senhas devem ser idênticas.'})
        users = Users (
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            password = password
        )
        users.save()

        user_pk = Users.objects.get(id = users.pk)

        Token.objects.create(user=user_pk)

        return Response({"Sucesso":"Usuário Criado com Sucesso!"}, status=status.HTTP_201_CREATED)