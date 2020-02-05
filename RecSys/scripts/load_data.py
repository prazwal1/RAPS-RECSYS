import csv
from RecApp.models import Product
def run():
    fhand = open('RecApp/database_f.csv')
    reader = csv.reader(fhand)
    next(reader)
    Product.objects.all().delete()
    for row in reader:
        Product.objects.get_or_create(product_id=row[0],product_name=row[1],product_weight_g=row[3],product_length_cm=row[4],product_height_cm=row[5],product_width_cm=row[6],product_category=row[2],price=row[7],ratings = row[8])