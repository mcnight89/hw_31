from unicodedata import category

import factory.django
from django.template.defaultfilters import length

from ads.models import User, Category, Ad


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker('name')
    is_published = factory.Faker('boolean')
    category_id = factory.SubFactory(CategoryFactory)
    author_id = factory.SubFactory(UserFactory)
    price = 200
