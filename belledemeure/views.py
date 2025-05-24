from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,permissions
from .models import Property
from .serializers import PropertySerializer



@api_view(['GET'])
def home(request):
    return Response({'messege':'Wellcome to belledemeure '})

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Create your views here.
