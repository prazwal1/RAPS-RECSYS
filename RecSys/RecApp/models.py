from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    product_weight_g = models.FloatField()
    product_length_cm = models.FloatField()
    product_height_cm = models.FloatField()
    product_width_cm = models.FloatField()
    product_category = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    def get_absolute_url(self):
        return reverse('Productdetail', args=[str(self.product_id)])
    class Meta:
        ordering = ['?']