from django.urls import path
from . import views

urlpatterns = [
        path('', views.PostPageView.as_view(), name='blogpost'),
        path('posts/new', views.BlogCreateView.as_view(), name='post_new'),
        path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='blogdetails'),
        path('posts/', views.ArticlePageView.as_view(), name='articles'),        
        path('posts/', views.ArticleDetailView.as_view(), name='articledetails'),


]
