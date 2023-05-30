from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin

from api.models import User, Client, Event, Contract
from .permissions import IsSalesmanContract

from .serializers import (UserSerializer, MyTokenObtainPairSerializer, ContractSerializer, ClientSerializer)

class UserViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ContractViewset(ModelViewSet):
    permission_classes = (IsAuthenticated,IsSalesmanContract)
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


class ClientViewset(ModelViewSet):
    permission_classes = (IsAuthenticated,IsSalesmanContract)
    serializer_class = ClientSerializer
    queryset = Contract.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
