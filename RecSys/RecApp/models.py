from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=150,db_index= True, unique= True)
    product_name = models.CharField(max_length=150)
    product_weight_g = models.FloatField()
    product_length_cm = models.FloatField()
    product_height_cm = models.FloatField()
    product_width_cm = models.FloatField()
    product_category = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places= 2, max_digits=8)
    def __str__(self):
        return self.product_id
    def get_absolute_url(self):
        return reverse('Productdetail', args=[str(self.pk)])
    class Meta:
        ordering = ['?']
class Feature(models.Model):
    product_id = models.CharField(max_length=150,db_index= True, unique= True)
    product_index = models.IntegerField()
    review_score = models.FloatField()
    seller_index = models.IntegerField()
    category_index = models.IntegerField()
    class Meta:
        ordering = ['product_index']
