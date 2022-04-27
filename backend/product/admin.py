from django.contrib import admin
from product.models import (
    MeasurementUnit, 
    MeasurementCategory,
    Product,
    Variant,)
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('id', 'name',)

admin.site.register(Product, ProductAdmin)

class MeasurementCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','si_unit')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name', 'si_unit')

admin.site.register(MeasurementCategory, MeasurementCategoryAdmin)

class MeasurementUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'category', 'si_unit_coversion')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(MeasurementUnit, MeasurementUnitAdmin)