from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catogery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}, {self.description}"
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.name}"   
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  
    image = models.ImageField(upload_to='product/', blank=True)
    brand = models.CharField(max_length=255)
    catogery = models.ForeignKey(Catogery,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title}" 
      