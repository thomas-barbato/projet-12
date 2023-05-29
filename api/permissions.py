from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import permissions

from api.models import User, Client, Event, Contract


class IsSalesmanClient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if view.kwargs["pk"]:
                return User.objects.filter(
                    user_id=request.user, role="SALES", contract=view.kwargs["pk"]
                ).exists()
            return True
        elif request.method in ["POST"]:
            return True
        elif request.method in ["PUT"]:
            if Client.objects.filter(id=view.kwargs["pk"]).exists():
                return obj.sales_contract_id == request.user.id and request.user.role == "SALES"
            raise ObjectDoesNotExist()
        return False


class IsSalesmanContract(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.method in ["PUT"]:
            if view.kwargs["pk"]:
                if Contract.objects.filter(id=view.kwargs["pk"]).exists() is False:
                    raise ObjectDoesNotExist()
            return bool(obj.sales_contact_id == request.user.id and request.user.role == "SALES")
        return False

class IsSalesmanOrSupportEvent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.method in ["PUT"]:
            if view.kwargs["pk"]:
                if Event.objects.filter(id=view.kwargs["pk"]).exists() is False:
                    raise ObjectDoesNotExist()
            return bool(obj.support_contact_id == request.user.id and request.user.role == "SUPPORT")
        elif request.method in ["POST"]:
            if view.kwargs["pk"]:
                if Contract.objects.filter(id=view.kwargs["pk"]).exists() is False:
                    raise ObjectDoesNotExist()
            return bool(obj.sales_contact_id == request.user.id and request.user.role == "SALES")
        return False

#pas sur...
class IsSupportClient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if view.kwargs["pk"]:
                if Event.objects.filter(id=view.kwargs["pk"]).exists() is False:
                    raise ObjectDoesNotExist()
            return bool(obj.support_contact_id == request.user.id and request.user.role == "SUPPORT")



