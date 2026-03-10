from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .tasks import send_order_email, send_order_cancel_email


@receiver(post_save, sender=Order)
def order_status_handler(sender, instance, created, **kwargs):

    # Order yangi yaratilganda
    if created:
        send_order_email.delay(
            instance.user.email,
            instance.id
        )

    # Order cancel bo‘lsa
    elif instance.status == "cancelled":
        send_order_cancel_email.delay(
            instance.user.email,
            instance.id
        )