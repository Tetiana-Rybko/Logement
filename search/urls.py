from django.urls import path
from .views import PropertySearchView

urlpatterns = [
    path('', PropertySearchView.as_view(), name='property-search'),
]