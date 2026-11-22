from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products, timeout=1)
    return products


def get_products_by_category(category_id):

    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    cache_key = f"category_{category_id}"
    products = cache.get(cache_key)

    if products is not None:
        return products
    products = Product.objects.filter(
        category_id=category_id, bool_publication=True
    ).select_related("category", "owner")
    cache.set(cache_key, products, timeout=1)

    return products


def clear_products_cache():
    key = "product_list"
    cache.delete(key)
