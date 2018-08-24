from django.urls import path
from . import views


urlpatterns = [
        path('coursehome', views.CourseHome, name='coursehome'),
        path('courseadd', views.CourseAdd, name='courseadd'),
        path('courseremoverequest', views.RemoveCourseRequest, name='courseremoverequest'),
        path('courseremove', views.RemoveCourse, name='courseremove'),
    
]
