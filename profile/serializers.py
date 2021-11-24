from profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']