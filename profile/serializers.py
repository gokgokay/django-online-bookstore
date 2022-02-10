from profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['username', 'bio', 'phone', 'country', 'image']
        read_only_fields = ('username',)

