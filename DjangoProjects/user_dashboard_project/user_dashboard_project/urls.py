from django.contrib import admin
from django.conf.urls import include 
from django.urls import path

admin.site.site_header = "Coding Dojo Admin"
admin.site.site_title = "Coding Dojo Admin Portal"
admin.site.index_title = "Welcome to UMSRA Research Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls')),
    path('accounts/', include('apps.authentication_and_authorization.urls'))
]



