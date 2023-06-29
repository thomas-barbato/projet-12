from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from api.views import (
    ClientDetailViewset,
    ClientListViewset,
    ContractDetailViewset,
    ContractListViewset,
    EventDetailViewset,
    EventListViewset,
    MyTokenObtainPairView,
    UserViewset,
)

client_pattern = [
    path("", ClientListViewset.as_view(), name="list"),
    path("<int:pk>", ClientDetailViewset.as_view(), name="details"),
]

contract_pattern = [
    path("", ContractListViewset.as_view(), name="list"),
    path("<int:pk>", ContractDetailViewset.as_view(), name="details"),
]

event_pattern = [
    path("", EventListViewset.as_view(), name="list"),
    path("<int:pk>", EventDetailViewset.as_view(), name="details"),
]

urlpatterns = [
    path("clients/", include(client_pattern)),
    path("contracts/", include(contract_pattern)),
    path("events/", include(event_pattern)),
    path("signup/", UserViewset.as_view({"post": "create"}), name="signup"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
