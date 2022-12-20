from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_api.serializers import UserSerializer, HomeSerializer

from home_page.models import Home


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [permissions.IsAuthenticated]
