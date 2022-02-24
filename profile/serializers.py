from profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['username', 'bio', 'phone', 'follower_count', 'following_count']
        read_only_fields = ('username', 'follower_count', 'following_count')

