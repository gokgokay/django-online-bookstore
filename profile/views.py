from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .serializers import ProfileSerializer


class ListProfileView(ListAPIView):
    pass


class ProfileFollowAPIView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def __delete__(self, instance):
        pass

    def post(self, request, username=None):
        pass

