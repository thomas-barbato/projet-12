from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Client, Contract, Event, User

from .permissions import (
    IsSalesmanClient,
    IsSalesmanContract,
    IsSalesmanOrSupportEvent,
    IsSupportClient,
)
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
    MyTokenObtainPairSerializer,
    UserSerializer,
)


class UserViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ContractListViewset(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsSalesmanContract)
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = filterset_fields = [
        "date_created",
        "amount",
        "client__email",
        "client__first_name",
        "client__last_name",
        "client__company_name",
    ]

    def get_queryset(self):
        if self.request.user.role == "SALES":
            return Contract.objects.filter(sales_contact=self.request.user)
        return Contract.objects.all()


class ContractDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsSalesmanContract)
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

    def update(self, request, *args, **kwargs):
        contract = self.get_object()
        serializer = ContractSerializer(data=request.data, instance=contract)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ClientListViewset(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSalesmanClient | IsSupportClient]
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = search_fields = ["first_name", "last_name", "email"]

    def get_queryset(self):
        if self.request.user.role == "SUPPORT":
            return Client.objects.filter(
                event__support_contact=self.request.user
            ).distinct()
        elif self.request.user.role == "SALES":
            return Client.objects.filter(contract__sales_contact=self.request.user)
        return Client.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSalesmanClient | IsSupportClient]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def update(self, request, *args, **kwargs):
        client = self.get_object()
        serializer = ClientSerializer(data=request.data, instance=client)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class EventListViewset(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsSalesmanOrSupportEvent)
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = search_fields = [
        "event_date",
        "client__email",
        "client__first_name",
        "client__last_name",
    ]

    def get_queryset(self):
        if self.request.user.role == "SUPPORT":
            return Event.objects.filter(support_contact=self.request.user)
        return Event.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsSalesmanOrSupportEvent)
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def update(self, request, *args, **kwargs):
        contract = self.get_object()
        serializer = EventSerializer(data=request.data, instance=contract)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
