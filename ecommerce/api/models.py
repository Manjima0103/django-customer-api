from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
