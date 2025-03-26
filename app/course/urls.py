from django.contrib import admin
from django.urls import include, path

# from .views import api_root, CourseDetailsView
from .views import CourseDetailsView


# Course Details View
course_details = CourseDetailsView.as_view({
    "get": "retreive",
    "post": "retreive_course_details"
})

urlpatterns = [
    # path("", api_root),
    path("course-details", course_details, name="course-details"),
]