from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, unique = True, blank = False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    variant_name = models.CharField(max_length=256)
    variant_description = models.TextField(blank = True)
    serial_number = models.CharField(max_length=256, blank=False)
    model = models.CharField(max_length=256)

    SIZE_CHOICES = [
            ("XS", "extra small"),
            ("S", "small"),
            ("M", "medium"),
            ("L", "large"),
            ("XL", "extra large"),
        ]
    size = models.CharField(choices = SIZE_CHOICES,max_length=256, blank = True)
    mass = models.DecimalField(max_digits=100, decimal_places=2)
    length = models.DecimalField(max_digits=100, decimal_places=2)
    width = models.DecimalField(max_digits=100, decimal_places=2)
    height = models.DecimalField(max_digits=100, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
