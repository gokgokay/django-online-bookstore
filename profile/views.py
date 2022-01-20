from rest_framework import serializers, status, generics
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from book.permissions import IsAdminUserOrReadOnly
from .models import Profile
from .renderer import ProfileJSONRenderer
from .serializers import ProfileSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    pass


class ProfileFollowAPIView(APIView):
    pass


class ProfileCreateList(generics.ListCreateAPIView):
    pass
