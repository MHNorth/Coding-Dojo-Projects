from django.urls import path
from . import views


urlpatterns = [
        path('', views.AmadonHome, name='home'),
        path('buy', views.AmadonBuy, name='purchase'),
        path('checkout', views.AmadonCheckout, name='checkout'),
        path('detail', views.AmadonDetail, name='detail'),
    
]
