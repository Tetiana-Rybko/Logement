from rest_framework import generics
from .serializers import UserReqisterSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status

User = get_user_model()

class HelloUserView(APIView):
    permission_classes = (IsAuthenticated)
    def get(self, request):
        return Response({"message": "Salut!"})


class UserRegisterView(APIView):
    serializer_class = UserReqisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserReqisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



