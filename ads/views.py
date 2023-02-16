import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ads.models import Ad, User, Category, Location
from ads.serializers import CategorySerializer, LocationSerializer, AdSerializer, UserSerializer, UserCreateSerializer, \
    CategoryDetailSerializer, AdDetailSerializer, UserDetailSerializer, LocationDetailSerializer, \
    LocationCreateSerializer, AdCreateSerializer, CategoryCreateSerializer
from djangoProject import settings


# Create your views here.
def start_page(request):
    return HttpResponse('БЕГИТЕ ГЛУПЦЫ')


# ===========================================================================
# CATEGORY #
# ===========================================================================
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)

        self.object.name = cat_data['name']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"DELETED"}, status=200)


# ===========================================================================
# ADS #
# ===========================================================================

class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', "author_id", "price", "description", "is_published", "image", "category_id"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        self.object.name = ad_data['name']
        self.object.author = ad_data['author_id']
        self.object.price = ad_data['price']
        self.object.description = ad_data['description']
        self.object.is_published = ad_data['is_published']
        self.object.image = ad_data['image']
        self.object.category_id = ad_data['category_id']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author_id.username,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            'image': self.image.url if self.object.image else None,
            'category_id': self.object.category_id.name

        })


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.image = request.FILES.get('image')
        ad.save()

        response = {
            'id': ad.id,
            'name': ad.name,
            'author': ad.author_id.username,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image.url if ad.image else None,
            'is_published': ad.is_published,
            'category_id': ad.category_id.name
        }

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"DELETED"}, status=200)


# ===========================================================================
# USERS #
# ===========================================================================


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', "last_name", "username", "password", "role", "age", "location_id"]

    def post(self, request, *args, **kwargs):
        user_data = UserCreateSerializer(data=json.loads(request.body))
        if user_data.is_valid():
            user_data.save()
        else:
            return JsonResponse(user_data.errors)

        return JsonResponse(user_data.data)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', "last_name", "username", "password", "role", "age", "location_id"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.role = user_data['role']
        self.object.age = user_data['age']
        self.object.location_id = user_data['location_id']

        self.object.save()

        return JsonResponse({
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
            'price': user_data.price,
            'password': user_data.password,
            'role': user_data.role,
            'age': user_data.age,
            'location_id': user_data.location_id

        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"DELETED"}, status=200)


# ===========================================================================
# LOCATION #
# ===========================================================================


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer


class LocationDetailView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LocationUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)

        self.object.name = cat_data['name']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class LocationDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"DELETED"}, status=200)
