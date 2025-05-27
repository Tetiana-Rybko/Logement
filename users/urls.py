from django.urls import path
from.views import UserRegisterView,HelloUserView,UserDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)


urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('hello/', HelloUserView.as_view(), name='hello-user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
