from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import User, Client, Event, Contract

from .serializers import (UserSerializer, MyTokenObtainPairSerializer)


class UserViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
