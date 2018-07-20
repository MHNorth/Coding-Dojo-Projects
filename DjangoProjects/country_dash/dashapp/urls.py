from django.urls import path, include
from . import views           # This line is new!

urlpatterns = [
    path("dashapp", views.index)
    # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon
