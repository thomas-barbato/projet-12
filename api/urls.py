from django.urls import include, path
from django.contrib import admin
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from api.views import (MyTokenObtainPairView, UserViewset)

base_router = routers.DefaultRouter()

urlpatterns = [
    path("", include(base_router.urls)),
    path('admin/', admin.site.urls),
    path("signup/", UserViewset.as_view({"post": "create"}), name="signup"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]