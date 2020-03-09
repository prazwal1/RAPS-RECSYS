from django import template
from ..Recommender import PopularityBasedRecommender

register = template.Library()
@register.simple_tag
def Popular_item():
    p = PopularityBasedRecommender()
    items = p.get_recommendation()
    return items