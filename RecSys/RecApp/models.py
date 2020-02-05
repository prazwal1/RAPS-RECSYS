from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=150,db_index= True)
    product_name = models.CharField(max_length=150)
    product_weight_g = models.FloatField()
    product_length_cm = models.FloatField()
    product_height_cm = models.FloatField()
    product_width_cm = models.FloatField()
    product_category = models.CharField(max_length=100)
    price = models.FloatField(null= True)
    ratings = models.FloatField(null= True)

    def get_absolute_url(self):
        return reverse('Productdetail', args=[str(self.pk)])
    class Meta:
        ordering = ['?']