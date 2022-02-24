from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ListProfileView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    ordering_fields = 'timestamp'
