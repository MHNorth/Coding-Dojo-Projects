from django.urls import path
from . import views


urlpatterns = [
        path('', views.CourseHome, name='coursehome'),
        path('courseadd', views.CourseAdd, name='courseadd'),
        path('courseremoverequest', views.RemoveCourseRequest, name='courseremoverequest'),
        path('courseremove/<int:course_id>', views.RemoveCourse, name='courseremove'),
    
]
