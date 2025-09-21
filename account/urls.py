from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterViewSet

router = DefaultRouter()
router.register(r'register', UserRegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]