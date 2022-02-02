from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from profile.serializers import ProfileSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(**data)
        if user is None:
            raise serializers.ValidationError('User was not found')

        return {'email': user.email, 'username': user.username}
