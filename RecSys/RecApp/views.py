from django.shortcuts import render , get_object_or_404
from .models import Product
from django.core.paginator import Paginator
from django.views.generic import DetailView,ListView
    
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"
    paginate_by = 40
    queryset = Product.objects.all()



    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['product_id'] = product_id
#        context['product_name'] = product_name
#        context['product_weight_g'] = product_weight_g
#        context['product_length_cm'] = product_length_cm
#        context['product_height_cm'] = product_height_cm
#        context['product_width_cm'] = product_width_cm
#        context['product_category'] = product_category
#        context['price'] = price
#        return context
class Productdetail(DetailView):
    model = Product
    template_name = 'product-page.html'