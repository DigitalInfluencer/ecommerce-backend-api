from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from .models import Order
import requests


@shared_task
def cancel_unpaid_orders():

    time_threshold = timezone.now() - timedelta(minutes=30)

    orders = Order.objects.filter(
        status="pending",
        created_at__lt=time_threshold
    )

    count = orders.count()

    for order in orders:
        order.status = "cancelled"
        order.save()

        # cancellation email
        send_order_cancel_email.delay(
            order.user.email,
            order.id
        )

    return f"{count} orders cancelled"


@shared_task
def send_order_email(user_email, order_id):

    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {settings.RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": settings.FROM_EMAIL,
            "to": [user_email],
            "subject": f"Order #{order_id} Confirmation",
            "html": f"""
                <h2>Order Confirmation</h2>
                <p>Your order <b>#{order_id}</b> has been placed successfully.</p>
                <p>Thank you for shopping with us!</p>
            """
        }
    )

    return {
        "status_code": response.status_code,
        "message": "Order email sent"
    }


@shared_task
def send_order_cancel_email(user_email, order_id):

    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {settings.RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": settings.FROM_EMAIL,
            "to": [user_email],
            "subject": f"Order #{order_id} Cancelled",
            "html": f"""
                <h2>Order Cancelled</h2>
                <p>Your order <b>#{order_id}</b> has been cancelled.</p>
                <p>If you have any questions please contact support.</p>
            """
        }
    )

    return {
        "status_code": response.status_code,
        "message": "Cancel email sent"
    }