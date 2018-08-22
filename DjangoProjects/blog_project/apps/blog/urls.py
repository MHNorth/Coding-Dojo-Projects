from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('about', views.about, name='about'),
        path('shop', views.shop, name='shop'),
        path('register', views.register, name='register'),
        path('login', views.login, name='login'),
        path('logout', views.logout, name='logout'),

]

