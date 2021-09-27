from rest_framework import  serializers

from ..models import Users, Farms, Seasons

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True}
        }
        model = Users
        fields = (
            'id',
            'name',
            'email',
            'password',
            'created',
            'modified'
        )
        

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