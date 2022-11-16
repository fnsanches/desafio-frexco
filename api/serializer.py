from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from base.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length= 200,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": 
            {
                "required": False, 
                "allow_null": True,
            }}
        
    def create(self, validated_data):
        username=validated_data['username']
        birthdate=validated_data['birthdate']  
        
        if 'password' in validated_data:
            password = validated_data['password']
        else:
            password = get_random_string(length=12)
        user = User(
            username=username,
            password=password,
            birthdate=birthdate  
        )
        
        user.save()
        return user