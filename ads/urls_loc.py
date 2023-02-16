from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('', views.LocationListView.as_view()),
    path('<int:pk>/', views.LocationDetailView.as_view()),
    path('create/', views.LocationCreateView.as_view()),
    path('<int:pk>/update/', views.LocationUpdateView.as_view()),
    path('<int:pk>/delete/', views.LocationDeleteView.as_view()),
]
