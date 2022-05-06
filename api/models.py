from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    img = models.ImageField()


class Info(models.Model):
    phone = models.IntegerField()
    location = models.CharField(max_length=255)
    day_time = models.DateTimeField()
    tw = models.URLField()
    fb = models.URLField()
    insta = models.URLField()


class welcome_text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()


class Service(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField(Category)
    img = models.ImageField()

    def __str__(self):
        return self.name

class Achievement(models.Model):
    icon = models.ImageField()
    num = models.IntegerField()
    name = models.CharField(max_length=255)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Blog(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ManyToManyField(Category)


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.TextField()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.product.name