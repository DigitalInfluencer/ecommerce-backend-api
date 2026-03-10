from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}, {self.street}"