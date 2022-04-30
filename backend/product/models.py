from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

class MeasurementCategory(models.Model):
    name = models.CharField( max_length=256)
    si_unit = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)
    
    class Meta:
        verbose_name_plural = "Measurement categories"

class MeasurementUnit(models.Model):
    name =models.CharField( max_length=256)
    symbol = models.CharField( max_length=3)
    category = models.ForeignKey(MeasurementCategory, on_delete=models.CASCADE)
    si_unit_coversion = models.DecimalField(max_digits=100, decimal_places=4)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

class Product(models.Model):
    name = models.CharField(max_length=256, unique = True, blank = False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)
    

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    variant_name = models.CharField(max_length=256)
    variant_description = models.TextField(blank = True)
    serial_number = models.CharField(max_length=256, blank=False)
    model = models.CharField(max_length=256)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    SIZE_CHOICES = [
            ("XS", "extra small"),
            ("S", "small"),
            ("M", "medium"),
            ("L", "large"),
            ("XL", "extra large"),
        ]
    size = models.CharField(choices = SIZE_CHOICES,max_length=256, blank = True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.variant_name)


