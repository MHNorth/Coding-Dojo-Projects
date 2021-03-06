from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home,  name='home'),
    path('fashion', views.Fashion,  name='fashion'),
    path('model', views.Model,  name='model'),
    path('travel', views.Travel,  name='travel'),
    path('about', views.About,  name='about'),
    path('contact', views.Contact,  name='contact'),
    path('blog', views.BlogPage,  name='blogpage'),
    path('post', views.PostDetail, name='postdetail'),
    path('post/new', views.New, name='postnew'),
    path('post/edit', views.Edit, name='postedit'),
    path('drafts', views.Drafts, name='postdraft'),
    path('post/remove', views.PostRemove, name='postremove'),
    path('post/publish', views.Publish, name='registerhome'),
    path('post/comment', views.Comment, name='registerhome'),
    path('comment/approve', views.Approve, name='registerhome'),
    path('comment/remove', views.CommentRemove, name='registerhome'),
]
