from drf_yasg.utils import swagger_auto_schema
from .serializers import UserDetailSerializer,UserRegisterSerializer,MyTokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class HelloUserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({"message": "Salut!"})


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer