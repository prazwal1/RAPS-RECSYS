from django.contrib import admin

# Register your models here.
from .models import Product ,Feature
admin.site.register(Product)
admin.site.register(Feature)
