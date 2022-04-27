from django.db import models

# Create your models here.
class MeasurementCategory(models.Model):
    name = models.CharField( max_length=256)
    si_unit = models.CharField(max_length=256)

    def __str__(self):
        return (self.name)
    
    class Meta:
        verbose_name_plural = "Measurement categories"

class MeasurementUnit(models.Model):
    name =models.CharField( max_length=256)
    symbol = models.CharField( max_length=3)
    category = models.ForeignKey(MeasurementCategory, on_delete=models.CASCADE)
    si_unit_coversion = models.DecimalField(max_digits=100, decimal_places=4)

    def __str__(self):
        return (self.name)

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
    mass = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # mass_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # length_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    width = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # width_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # height_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    diameter = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # diameter_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    thickness = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # thickness_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.variant_name)


