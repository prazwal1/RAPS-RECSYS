from sklearn.metrics.pairwise import cosine_similarity
import random
def get_product_id(iid):
    from .models import Feature
    product = Feature.objects.get(pk=iid)
    return product.product_id
def get_item_ids():
    from .models import Feature
    feature = Feature.objects.all()
    vector = []
    for obj in feature:
        vector.append(obj.product_index)
    return vector
def get_vector():
    from .models import Feature
    product = Feature.objects.all()
    vector = []
    for obj in product:
        vector.append(list([obj.seller_index,obj.category_index,obj.review_score]))
    return vector
def get_item_vector(iid):
    from .models import Feature
    feat = Feature.objects.get(pk = iid)
    vector = [[feat.seller_index,feat.category_index,feat.review_score]]
    return vector
def get_item_id(pid):
    from .models import Feature
    feature = Feature.objects.get(product_id = pid)
    item_id = feature.product_index
    return item_id
def get_review_score():
    from .models import Feature
    obj = Feature.objects.order_by('-review_score')
    obj = obj[:13970]
    items = list(obj)
    random.shuffle(items)
    return items[:10]
    


class ContentBasedRecommender:
    MODEL_NAME = "Content-Based"
    def __init__(self):
        self.vector = get_vector()
        self.item_ids = get_item_ids()
    def get_model_name(self):
        return self.MODEL_NAME
    def _get_similar_products(self,item_id,topn=100):
        cosine_similarities = cosine_similarity(get_item_vector(item_id),self.vector)
        similar_indices = cosine_similarities.argsort().flatten()
        similar_indices = similar_indices[-topn:]
        similar_products = sorted([(self.item_ids[i],cosine_similarities[0,i]) for i in similar_indices ], key=lambda x : -x[1])
        return similar_products
    def get_recommendation(self,item_id,items_to_ignore = [], topn = 10):
        items_to_ignore.append(item_id)
        similar_items = self._get_similar_products(item_id)
        similar_items_filtered = list(filter(lambda x: x[0] not in items_to_ignore, similar_items))
        products = []
        for i in range (0,5):
            products.append(get_product_id(similar_items_filtered[i][0]))
        return products

class PopularityBasedRecommender:
    MODEL_NAME = "Popularity-Based"
    def __init__(self):
        self.features = get_review_score()
    def get_recommendation(self):
        products = []
        for item in self.features:
            products.append(item.product_id)
        return products