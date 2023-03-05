
from django.urls import path


from ads.views import SelectionCreateView, SelectionListView

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('create/', SelectionCreateView.as_view()),
]
