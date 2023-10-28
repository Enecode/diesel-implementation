from .models import DieselData
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """user serializer for registration"""
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


class DieselDataSerializer(serializers.ModelSerializer):
    """diesel data serializer for list and create"""
    class Meta:
        model = DieselData
        fields = ['generator_id', 'fuel_level', 'timestamp']