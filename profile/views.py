from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ObjectDoesNotExist


class ListProfileView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    ordering_fields = 'timestamp'


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def post(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except ObjectDoesNotExist:
            raise NotFound('No profile found with this username.')

        if followee.is_followed_by(follower):
            raise serializers.ValidationError('You already follow this user.')

        if follower.pk is followee.pk:
            raise serializers.ValidationError('You can not follow yourself.')

        follower.follow(followee)

        serializer = self.serializer_class(followee, context={'request': request})

        return Response({
            'followee': serializer.data,
            'status': status.HTTP_201_CREATED})

    def delete(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except ObjectDoesNotExist:
            raise NotFound('No profile found with this username.')

        if not followee.is_followed_by(follower):
            raise serializers.ValidationError('You already unfollow this user.')

        if follower.pk is followee.pk:
            raise serializers.ValidationError('You can not unfollow yourself.')

        follower.unfollow(followee)

        serializer = self.serializer_class(followee, context={'request': request})

        return Response({
            'followee': serializer.data,
            'status': status.HTTP_200_OK})
