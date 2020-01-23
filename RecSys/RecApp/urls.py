from django.urls import path
from . import views
from .views import Productdetail

urlpatterns = [

    path('',views.home, name ='home'),
    path('product/<int:pk>/',Productdetail.as_view(), name='Productdetail')

]