from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
# Create your views here.

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer