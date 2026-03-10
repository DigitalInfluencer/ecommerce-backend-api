from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Product


# Clear cache when product is created or updated
@receiver(post_save, sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    cache.delete("product_list")
    cache.delete("top_rated_products")
    cache.delete("popular_products")


# Clear cache when product is deleted
@receiver(post_delete, sender=Product)
def clear_product_cache_on_delete(sender, instance, **kwargs):
    cache.delete("product_list")
    cache.delete("top_rated_products")
    cache.delete("popular_products")