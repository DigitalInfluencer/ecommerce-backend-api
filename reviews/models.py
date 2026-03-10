from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg

from products.models import Product

User = get_user_model()


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_product_rating()

    def delete(self, *args, **kwargs):
        product = self.product
        super().delete(*args, **kwargs)
        self.update_product_rating(product)

    def update_product_rating(self, product=None):

        product = product or self.product

        reviews = Review.objects.filter(product=product)

        avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"] or 0
        review_count = reviews.count()

        product.rating = avg_rating
        product.review_count = review_count
        product.save()

    def __str__(self):
        return f"{self.user} - {self.product} ({self.rating})"