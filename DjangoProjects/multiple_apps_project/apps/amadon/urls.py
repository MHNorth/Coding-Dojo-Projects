from django.urls import path
from . import views


urlpatterns = [
        path('amadonhome', views.AmadonHome, name='amadonhome'),
        path('amadonbuy', views.AmadonBuy, name='purchase'),
        path('amadoncheckout', views.AmadonCheckout, name='amadoncheckout'),
        path('amadondetail', views.AmadonDetail, name='amadondetail'),
    
]
