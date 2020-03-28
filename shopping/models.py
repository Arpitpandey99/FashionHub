from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class User_detail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Sub_category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.category.name +' -- '+self.name
class Product(models.Model):
    subcategory = models.ForeignKey(Sub_category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    discription = models.TextField(max_length=500,null=True)
    img1 = models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)

    def __str__(self):
        return self.subcategory.name + ' -- ' + self.name

class Add_to_cart(models.Model):
    usr = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

class Order_placed(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    address = models.TextField(null = True)





