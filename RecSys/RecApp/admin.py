from django.contrib import admin

# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_id',)} 
admin.site.register(Product,ProductAdmin)
