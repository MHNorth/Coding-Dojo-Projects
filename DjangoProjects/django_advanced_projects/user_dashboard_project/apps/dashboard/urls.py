from django.urls import path
from . import views


urlpatterns = [
        path('', views.DashHome, name='dashhome'),
        path('dash/admin', views.DashAdmin, name='dashadmin'),
        path('dash/editprofile', views.DashProfile, name='dashprofile'),
        path('dash/edituser', views.DashEdit, name='dashedit'),
        path('dash/newuser', views.DashNew, name='dashnew'),
        path('dash/user', views.DashUser, name='dashuser'),
        path('dash/userinfo', views.DashInfo, name='dashinfo'),
    
]
