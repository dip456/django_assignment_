from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=255)
