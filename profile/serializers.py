from profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    follows = serializers.CharField(source='user.username')
    favorites = serializers.CharField(source='book.name')
    bio = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Profile
        fields = ('username', 'follows', 'favorites', 'bio')
        read_only_fields = ('username',)
