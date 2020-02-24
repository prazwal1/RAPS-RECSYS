import csv
from RecApp.models import Feature , Product
def run():
    fhand = open('RecApp/features.csv')
    reader = csv.reader(fhand)
    next(reader)
    Feature.objects.all().delete()
    for row in reader:
        Feature.objects.create(product_id = row[1],product_index = row[0], seller_index = row[3], category_index = row[4], review_score = row[2])