from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.views.generic import (
    DetailView
)
# Create your views here.

def home(request):
    
    products = Product.objects.all()
    paginator = Paginator(products, 20)
    page = request.GET.get('page')

    products = paginator.get_page(page)

    return render(request, 'home.html',{'products':products})

class Productdetail(DetailView):
    model = Product