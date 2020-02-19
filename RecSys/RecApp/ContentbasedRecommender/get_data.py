from models import Feature, Product
def get_feature(pid):
    feature = Feature(product_id=pid)
    return feature
def get_product(pid):
    product = Product(product_id=pid)
    return product
