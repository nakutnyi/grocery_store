from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10_000)

