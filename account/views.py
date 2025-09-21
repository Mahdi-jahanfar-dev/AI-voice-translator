from rest_framework import viewsets, mixins, status
from account.serializers import UserRegisterSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": self.get_serializer(user).data}, status=status.HTTP_201_CREATED)