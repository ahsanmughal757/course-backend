from rest_framework import serializers

# import utils.course_utils as course_utils 
from .models import Course


class SupabaseConnectionSerializer(serializers.Serializer):
    url = serializers.URLField()
    key = serializers.CharField(max_length=200)

class CourseDetailsSerializer(serializers.Serializer):    
    playlist_url = serializers.URLField()
    level = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=200)
    prerequisites = serializers.JSONField(default=list)
    
    def create(self, validated_data):
        return validated_data
   
   

