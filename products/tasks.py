from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import CartItem


@shared_task
def clear_old_cart_items():

    time_threshold = timezone.now() - timedelta(minutes=20)

    old_items = CartItem.objects.filter(created_at__lt=time_threshold)

    count = old_items.count()

    old_items.delete()

    return f"{count} cart items deleted"