from profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image')
        read_only_fields = ('username',)
