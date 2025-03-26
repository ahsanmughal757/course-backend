from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    description = models.TextField()
    video_id = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200)
    category = models.CharField(max_length=200)
    duration = models.TextField()
    level = models.CharField(max_length=200)
    prerequisites = models.JSONField(default=list)
    rating = models.FloatField(default=0.0)
    students = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    # class Meta:
    #     ordering = ['created_at']
