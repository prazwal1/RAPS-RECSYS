from django import template
from ..Recommender import PopularityBasedRecommender,ReviewBasedRecommender

register = template.Library()
@register.simple_tag
def Popular_item():
    p = PopularityBasedRecommender()
    items = p.get_recommendation()
    return items
@register.simple_tag
def highest_ratings():
    h = ReviewBasedRecommender()
    items = h.get_recommendation()
    return items