from django.shortcuts import render
from .serialization import *
from rest_framework import generics, viewsets

# Create your views here.
class product_view(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class allProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


