from django.urls import path
from . import views


urlpatterns = [
        path('userhome', views.UserHome, name='userhome'),
        path('useradd', views.UserAdd, name='useradd'),
        path('useredit', views.UserEdit, name='useredit'),
        path('usershow', views.UserShow, name='usershow'),
]
