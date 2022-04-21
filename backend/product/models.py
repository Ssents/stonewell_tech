from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, unique = True, blank = False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=256)

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    mass = models.IntegerField()
    serial_number = models.CharField(max_length=256, blank=False)