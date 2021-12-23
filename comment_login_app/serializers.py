from rest_framework import serializers
from .models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'name', 'email']


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'name', 'email']


class SchemaView(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
