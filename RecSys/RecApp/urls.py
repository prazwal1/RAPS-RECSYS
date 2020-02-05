from django.urls import path
from . import views
from .views import Productdetail

urlpatterns = [

    path('',views.ProductList.as_view(), name ='home'),
    path('product/<int:pk>/',Productdetail.as_view(), name='Productdetail'),

]