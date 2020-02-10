from django.shortcuts import render , get_object_or_404
from .models import Product
from django.core.paginator import Paginator
from django.views.generic import DetailView,ListView
    
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "home.html"
    paginate_by = 16
class Productdetail(DetailView):
    model = Product
    template_name = 'product-page.html'