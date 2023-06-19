from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import User, Client, Event, Contract
from .permissions import IsSalesmanContract, IsSalesmanOrSupportEvent, IsSalesmanClient, IsSupportClient

from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    ContractSerializer,
    ClientSerializer,
    EventSerializer,
)


class UserViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ContractViewset(ModelViewSet):
    permission_classes = (IsAuthenticated, IsSalesmanContract)
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


class ClientViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSalesmanClient | IsSupportClient]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class EventViewset(ModelViewSet):
    permission_classes = (IsAuthenticated, IsSalesmanOrSupportEvent)
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
