from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),  # name='home' is often used in html files as links
        path('about', views.about, name='about'),
]
