from django.contrib.auth.models import Group, User
from rest_framework.views import APIView
from rest_framework import permissions, viewsets, status

from rest_framework.response import Response
from app.auth.serializers import GroupSerializer, UserSerializer

from django.contrib.auth import authenticate


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
    
    
class Login(APIView):
    
    def get(self, request):
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
        
        return Response({
            "message": "Login successful.",
        }, status=status.HTTP_200_OK)
        
        pass
    
    def post():
        pass