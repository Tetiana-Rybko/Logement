from django.urls import path
from .views import UserRegisterView,HelloUserView,UserDetailView,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('hello/', HelloUserView.as_view(), name='hello-user'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    #path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
