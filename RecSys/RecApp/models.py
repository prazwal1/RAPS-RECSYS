from django.db import models
from django.urls import reverse
from django_random_queryset import RandomManager
from .Recommender import ContentBasedRecommender,get_item_id
# Create your models here.
class Product(models.Model):
    objects = RandomManager()
    product_id = models.CharField(max_length=150,db_index= True, primary_key= True)
    product_name = models.CharField(max_length=150)
    product_weight_g = models.FloatField()
    product_length_cm = models.FloatField()
    product_height_cm = models.FloatField()
    product_width_cm = models.FloatField()
    product_category = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places= 2, max_digits=8,null=True)
    def __str__(self):
        return self.product_name
    def get_absolute_url(self):
        return reverse('Productdetail', args=[str(self.pk)])
    class Meta:
        ordering = ['?'] 
    

    def get_review_score(self):
        item = Feature.objects.get(product_id=self.product_id)
        return item.review_score
    def recommend(self):
        x = ContentBasedRecommender()
        item_id = get_item_id(self.pk)
        recommendation = x.get_recommendation(item_id)
    
        return recommendation
class Feature(models.Model):
    objects = RandomManager()
    product_id = models.OneToOneField(Product,max_length=150,db_index= True, unique= True,on_delete=models.CASCADE)
    product_index = models.IntegerField(primary_key=True)
    review_score = models.FloatField()
    seller_index = models.IntegerField()
    category_index = models.FloatField()
    sales_count = models.IntegerField(null= True)
    class Meta:
        ordering = ['product_index']
