from profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    follows = serializers.CharField(read_only=True)
    favorites = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'follows', 'favorites', 'bio']
