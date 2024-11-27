from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)


