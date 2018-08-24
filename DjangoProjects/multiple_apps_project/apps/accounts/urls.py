# from collection.backends import MyRegistrationView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('regcomplete', views.registercomp, name='rcomplete'),
    path('userlogout', views.logout, name='loggedout'),

]