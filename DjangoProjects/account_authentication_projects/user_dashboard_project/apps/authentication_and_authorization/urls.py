# from collection.backends import MyRegistrationView
from django.urls import path
from . import views

urlpatterns = [
    path('register/home', views.index, name='registerhome'),
    path('register', views.register, name='register'),
    path('log', views.log, name='getlog'),
    path('login', views.login, name='login'),
    path('register/complete', views.registercomp, name='rcomplete'),
    path('user/logout', views.logout, name='signout'),

]