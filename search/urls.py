from django.urls import path
from .views import SearchQueryHistoryView, PropertySearchView


urlpatterns = [
    path('', PropertySearchView.as_view(), name='property-search'),
    path('', PropertySearchView.as_view(), name='property-search'),
    path('history/', SearchQueryHistoryView.as_view(), name='search-history'),
]