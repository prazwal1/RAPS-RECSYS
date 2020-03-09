import csv
from RecApp.models import Feature , Product
def run():
    fhand = open('RecApp/final_features.csv')
    reader = csv.reader(fhand)
    next(reader)
    Feature.objects.all().delete()
    for row in reader:
        Feature.objects.create(product_id = row[1],product_index = row[0], seller_index = row[2], category_index = row[3], review_score = row[4])