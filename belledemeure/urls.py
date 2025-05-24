
from django.urls import path,include
from .views import  home,PropertyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'properties', PropertyViewSet,basename='property')



urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),

]