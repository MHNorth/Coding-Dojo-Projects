from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('travels/<int:user_id>', views.travels),
    path('trips', views.trips),
    # path('trips', views.trips),
    path('add_trip', views.add_trip),
    path('add', views.add),
    path('logout', views.logout),
    path('trip/<int:trip_id>', views.showtrip),
    path('join/<int:trip_id>', views.jointrip),
    path('leave/<int:trip_id>', views.leave_trip),
    path('delete/<int:trip_id>', views.delete_trip)

    # path('dashboard/<int:user_id>', views.dashboard),
    # path('dashboard', views.dashboard),
    # path('add', views.add),
    
    # path('join_trip/<int:trip_id>', views.join_trip),
    # path('remove/<int:trip_id>', views.remove)
]