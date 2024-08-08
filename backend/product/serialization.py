from rest_framework import serializers
from .models import *

class CategorySerializations(serializers.ModelSerializer):
    class Meta:
        models=Catogery
        fields= "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'brand', 'image', 'price', 'is_slider', 'is_featured']