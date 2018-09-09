"""multiple_apps_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import re_path
from django.contrib.sitemaps.views import sitemap
# from multiple_apps.sitemap import ThingSitemap, StaticSitemap, HomepageSitemap
# sitemaps = {
# 'things': ThingSitemap,
# 'static': StaticSitemap,
# 'homepage': HomepageSitemap,
# }



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.multiple_apps.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            }),
            ]

