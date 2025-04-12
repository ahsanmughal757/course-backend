from django.contrib.auth.models import Group, User
from rest_framework.views import APIView
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from app.auth.serializers import GroupSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from pprint import pprint

from django.contrib.auth import authenticate

import logging
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class LoginAPIView(APIView):

    queryset = User.objects.all()
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
    
        if not username or not password:
            return Response({
                "detail": "Please provide username and password."
                }, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response({
                "detail": "Invalid credentials."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        
        # Generate the token for the user
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            "message": "Login successful.",
            "token": token.key,
            "user": {
                "username": user.username,
                "email": user.email
            }
        }, status=status.HTTP_200_OK)
        
        
class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response({
                "detail": "User is not logged in."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            "detail": "Logged out successfully."
        }, status=status.HTTP_200_OK)
        


class SessionAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        user = request.user        
        session_user = User.objects.get(username=user)

        return Response({
            "user": session_user.email,
            "message": "Session retrieved successfully",
            "code": "SESSION_RETRIEVED",
        }, status=status.HTTP_200_OK)