from django.urls import path
from . import views


urlpatterns = [
        path('wallhome', views.WallHome, name='wallhome'),
    
]
