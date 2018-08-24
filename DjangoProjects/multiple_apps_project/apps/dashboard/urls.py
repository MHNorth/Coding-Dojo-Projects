from django.urls import path
from . import views


urlpatterns = [
        path('dashhome', views.DashHome, name='dashhome'),
        path('dashadmin', views.DashAdmin, name='dashadmin'),
        path('dasheditprofile', views.DashProfile, name='dashprofile'),
        path('dashedituser', views.DashEdit, name='dashedit'),
        path('dashnewuser', views.DashNew, name='dashnew'),
        path('dashregister', views.DashRegister, name='dashregister'),
        path('dashsignin', views.DashSign, name='dashsign'),
        path('dashuser', views.DashUser, name='dashuser'),
        path('dashuserinfo', views.DashInfo, name='dashinfo'),
    
]

