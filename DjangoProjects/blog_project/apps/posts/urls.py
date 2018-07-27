from django.urls import path
from . import views

urlpatterns = [
        path('posts/', views.PostPageView.as_view(), name='blogpost'),
        path('posts/', views.ArticlePageView.as_view(), name='articles'),
        path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='blog_details'),
        path('posts/', views.ArticleDetailView.as_view(), name='article_details'),


]
