from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("apps.blog.urls")),
    path('posts/', include("apps.posts.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
