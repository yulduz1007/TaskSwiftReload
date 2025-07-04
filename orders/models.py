from django.db import models
from django.db.models import ForeignKey

from products.models import Product
from users.models import User


# Create your models here.

class Order(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.product}"
