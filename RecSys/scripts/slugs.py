from RecApp.models import Product
def run():
    obj = Product.objects.all()
    for a in obj:
        a.slug = a.product_id
        a.save()