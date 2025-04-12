from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import CourseDetailsSerializer, SupabaseConnectionSerializer


from django.contrib.auth.models import User
from .models import Course
from .utils.course_utils import get_playlist_data

# View for Course Details
class CourseDetailsView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Course.objects.all()
    serializer_class = CourseDetailsSerializer    
    def retreive(self, request):
        courses = Course.objects.all()
        serializer = CourseDetailsSerializer(courses, many=True)
        return Response(serializer.data)
    
    def retreive_course_details(self, request):
        serializer = CourseDetailsSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            playlist_url = serializer.data['playlist_url']
            course_level = serializer.data['level']
            course_category = serializer.data['category']
            prerequisites = serializer.data['prerequisites']
            
            playlist_data = get_playlist_data(playlist_url, course_level, course_category, prerequisites)
             
            return Response(playlist_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)