from rest_framework import generics
from .serializers import UserReqisterSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class HelloUserView(APIView):
    def get(self, request):
        return Response({"message": "Salut!"})

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserReqisterSerializer





