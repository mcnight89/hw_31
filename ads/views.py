import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad, User, Category, Location
from ads.serializers import CategorySerializer, LocationSerializer, AdSerializer, UserSerializer, UserCreateSerializer, \
    CategoryDetailSerializer, AdDetailSerializer, UserDetailSerializer, LocationDetailSerializer, \
    LocationCreateSerializer, AdCreateSerializer, CategoryCreateSerializer, CategoryUpdateSerializer, \
    AdUpdateSerializer, UserUpdateSerializer, LocationUpdateSerializer, CategoryDestroySerializer, AdDestroySerializer, \
    UserDestroySerializer, LocationDestroySerializer
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

    def get(self, request, *args, **kwargs):
        category_text = request.GET.get('name', None)
        if category_text:
            self.queryset = self.queryset.filter(
                name__icontains=category_text
            )

        return super().get(request, *args, **kwargs)


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDestroySerializer


# ===========================================================================
# ADS #
# ===========================================================================

class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        location = request.GET.get('location', None)
        if location:
            self.queryset = self.queryset.filter(
                author_id__location__name__icontains=location
            )

        category_ids = request.GET.getlist('category_id', None)
        category_id_q = None
        for cat in category_ids:
            if category_id_q is None:
                category_id_q = Q(category_id__in=cat)
            else:
                category_id_q |= Q(category_id__in=cat)
        if category_id_q:
            self.queryset = self.queryset.filter(category_id_q)

        price = request.GET.get('price', None)
        if price:
            self.queryset = self.queryset.filter(price__gte=price)
        else:
            self.queryset = self.queryset.filter(price__lte=price)

        return super().get(request, *args, **kwargs)


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


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


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer


# ===========================================================================
# USERS #
# ===========================================================================


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


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


class LocationUpdateView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer


class LocationDeleteView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDestroySerializer
