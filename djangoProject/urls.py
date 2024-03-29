"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads import views
from ads.views import LocationViewSet, CategoryViewSet
from djangoProject import settings

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('category', CategoryViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_page),
    path('ads/', include('ads.urls_ad')),
    path('users/', include('ads.urls_user')),
    path('selection/', include('ads.urls_selection')),
    path('api_auth/', include('rest_framework.urls'))

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
