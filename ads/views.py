import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


# Create your views here.
def start_page(request):
    return HttpResponse('200 {"status": "ok"}')


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        cat = Category.objects.all()

        response = []
        for c in cat:
            response.append({
                'id': c.id,
                'name': c.name
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        cat_data = json.loads(request.body)

        category = Category()
        category.name = cat_data['name']
        category.save()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({
              'status': 'error'}, status=404)

        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ad = Ad.objects.all()

        response = []
        for a in ad:
            response.append({
                'id': a.id,
                'name': a.name,
                'author': a.author,
                'price': a.price,
                'description': a.description,
                'address': a.address,
                'is_published': a.is_published
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        ad_data = json.loads(request.body)

        ads = Ad()
        ads.name = ad_data['name']
        ads.author = ad_data['author']
        ads.price = ad_data['price']
        ads.description = ad_data['description']
        ads.address = ad_data['address']
        ads.is_published = ad_data['is_published']
        ads.save()

        return JsonResponse({
            'id': ads.id,
            'name': ads.name,
            'author': ads.author,
            'price': ads.price,
            'description': ads.description,
            'address': ads.address,
            'is_published': ads.is_published
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({
                'status': 'error'}, status=404)

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        })
