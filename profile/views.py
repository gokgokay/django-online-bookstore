from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ProfileSerializer


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def post(self, request, username=None):
        pass

    def delete(self, request, username=None):
        pass
