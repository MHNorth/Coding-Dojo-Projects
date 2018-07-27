from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import UserPost, ArticlePost


class PostPageView(ListView):    #ListView returns object_list. We will use this in our post template
    model = UserPost
    template_name='posts/mypost.html'
       

class BlogDetailView(DetailView):
    model = UserPost
    template_name='posts/post_detail.html'
    context_object_name = 'blogdetails'

class BlogCreateView(CreateView):
    model = UserPost
    template_name='posts/post_new.html'
    fields = '__all__'

class ArticlePageView(ListView):
    model = ArticlePost
    template_name='posts/articles.html'
    
class ArticleDetailView(DetailView):
    model = ArticlePost
    template_name='posts/article_detail.html'
    context_object_name = 'articledetails'
