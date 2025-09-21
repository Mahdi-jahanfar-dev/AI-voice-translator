from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]