from unicodedata import category
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

from ads.validators import check_age, check_email


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(null=True, max_length=10, unique=True,
                            validators=[MinLengthValidator(5), MaxLengthValidator(10)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    admin = 'admin'
    member = 'member'
    moderator = 'moderator'
    ROLES = [
        (admin, admin),
        (member, member),
        (moderator, moderator)
    ]
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(choices=ROLES, max_length=15, default='member')
    age = models.IntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True, validators=[check_age])
    email = models.EmailField(unique=True, null=True, validators=[check_email])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username


class Ad(models.Model):
    name = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(10)])
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=None)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-price"]

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=150)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
