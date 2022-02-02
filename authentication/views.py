from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .renderers import UserJSONRenderer
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    # renderer_classes = UserJSONRenderer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": serializer.data,
                         "status": status.HTTP_201_CREATED,
                         "token": user.token})


class LoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({"user": serializer.data,
                         "status": status.HTTP_200_OK})
