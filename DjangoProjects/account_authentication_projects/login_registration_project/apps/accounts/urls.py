# from collection.backends import MyRegistrationView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('log', views.log, name='getlog'),
    path('login', views.login, name='login'),
    path('regcomplete', views.registercomp, name='rcomplete'),
    path('userlogout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dash'),

]