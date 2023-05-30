from django.urls import include, path
from django.contrib import admin
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from api.views import (MyTokenObtainPairView, UserViewset, ContractViewset, ClientViewset)

base_router = routers.DefaultRouter()
# /contracts/
# /contracts/{pk}/
base_router.register(r"contracts", ContractViewset, basename="contract")
# /clients/
# /clients/{pk}/
base_router.register(r"clients", ClientViewset, basename="client")


urlpatterns = [
    path("", include(base_router.urls)),
    path('admin/', admin.site.urls),
    path("signup/", UserViewset.as_view({"post": "create"}), name="signup"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]