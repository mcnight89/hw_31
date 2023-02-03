from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ads.models import Category, Ad


# Create your views here.
def start_page(request):
    return HttpResponse('200 {"status": "ok"}')


def category_all(request):
    if request.method == "GET":
        cat = Category.objects.all()

        response = []
        for c in cat:
            response.append({
                'id': c.id,
                'name': c.name
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def get_category_id(request, category_id):
    if request.method == "GET":
        cat = Category.objects.get(pk=category_id)

        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })


def ad_all(request):
    if request.method == "GET":
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


def get_ad_id(request, ad_id):
    if request.method == "GET":
        ad = Ad.objects.get(pk=ad_id)

        return JsonResponse({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
        })


