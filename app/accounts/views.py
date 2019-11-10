from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from knox.models import AuthToken
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                "status": "success",
                "data": {
                    "message": "User account successfully created",
                    "token": str(refresh.access_token),
                    "userId": user.id
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)

            return Response({
                "status": "success",
                "data": {
                    "token": str(refresh.access_token),
                    "userId": user.id
                }

            }, status=status.HTTP_200_OK)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)


class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user


