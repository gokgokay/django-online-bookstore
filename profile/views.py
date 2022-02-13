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
        username = self.kwargs['username']
        import pdb;pdb.set_trace()
        try:
            followee = Profile.objects.get(user__username=username)  # check this line for getting followee
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found.')


        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)
