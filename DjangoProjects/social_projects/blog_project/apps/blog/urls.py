from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostHome, name='postlist'),
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
