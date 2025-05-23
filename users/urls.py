from django.urls import path
from.views import UserRegisterView,HelloUserView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('hello/', HelloUserView.as_view(), name='hello-user'),
]