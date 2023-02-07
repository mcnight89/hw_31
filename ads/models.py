from unicodedata import category

from django.db import models


# Create your models here.
# categ   id,name
# ad    id,name,author_id,price,description,is_published,image,category_id
# location id,name,lat,lng
# user id,first_name,last_name,username,password,role,age,location_id
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    # image = models.ImageField(upload_to='ads/', blank=True, null=True)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


# user id,first_name,last_name,username,password,role,age,location_id
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.IntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username
