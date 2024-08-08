from django.urls import path
from .views import *

urlpatterns = [
    path("", product_view.as_view({'get':'list'}), name="product" ),
    path("allproduct/", allProduct.as_view(), name="allproduct" )
]