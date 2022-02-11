from django.contrib.auth.models import User
from rest_framework import serializers, status, generics, mixins
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Profile
from .serializers import ProfileSerializer


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def post(self, request, username=None):
        follower = self.request.user

        try:
            followee = Profile.objects.get(user__username=username)  # check this line for getting followee
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found.')

        if follower.user.username is followee.user.username:
            raise serializers.ValidationError('You can not follow yourself.')
        follower.follow_user(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)
