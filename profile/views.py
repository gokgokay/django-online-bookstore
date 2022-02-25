from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from .models import Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ListProfileView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    ordering_fields = 'timestamp'


class UpdateRetrieveProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, AllowAny)

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user__username=self.kwargs.get('username'))
    