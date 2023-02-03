from django.db import models


# Create your models here.
# Id,name,author,price,description,address,is_published    id,name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Ad(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()
