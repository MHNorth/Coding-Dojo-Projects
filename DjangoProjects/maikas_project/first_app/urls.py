from django.urls import path, include
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog_post/', views.blog, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    path('recipe_post/', views.recipe, name='recipe_post'),
    ]