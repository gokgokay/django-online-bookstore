from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profile.models import Profile
from profile.renderer import ProfileJSONRenderer
from profile.serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
