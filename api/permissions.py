from rest_framework import permissions

from api.models import Contract, Event, Client

# doc here :
# https://stackoverflow.com/questions/43064417/whats-the-differences-between-has-object-permission-and-has-permission
# permission_classes are looped over the defined list.
#
# has_permission method will be called on all (GET, POST, PUT, DELETE) HTTP request.
#
# When a False value is returned from the permission_classes method,
# the request gets no permission and will not loop more, otherwise, it checks all permissions on looping.
#
# has_object_permission method is called after has_permission method returns value True except in POST method
# (in POST method only has_permission is executed).
#
# has_object_permission method will not be called on HTTP POST request, hence we need to
# restrict it from has_permission method.


class IsSalesmanClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" and view.kwargs:
            return Client.objects.filter(
                id=view.kwargs["pk"], sales_contact_id=request.user.id
            ).exists()
        elif request.method == "POST" and request.user.role == "SUPPORT":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Client.objects.filter(
            id=view.kwargs["pk"], sales_contact_id=request.user.id
        ).exists()


class IsSupportClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" and view.kwargs:
            return Event.objects.filter(
                client_id=view.kwargs["pk"], support_contact_id=request.user.id
            ).exists()
        elif request.method == "POST" and request.user.role == "SUPPORT":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


class IsSalesmanContract(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" and request.user.role != "SUPPORT":
            if view.kwargs:
                return Contract.objects.filter(
                    id=view.kwargs["pk"], sales_contact_id=request.user.id
                ).exists()
            return True
        elif request.method == "PUT":
            return Contract.objects.filter(
                id=view.kwargs["pk"], sales_contact_id=request.user.id
            ).exists()
        return False


class IsSalesmanOrSupportEvent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" and request.user.role != "SALES":
            if view.kwargs:
                return Event.objects.filter(
                    id=view.kwargs["pk"], support_contact_id=request.user.id
                ).exists()
            return True
        elif request.method in ["POST"] and request.user.role != "SUPPORT":
            return True
        elif request.method in ["PUT"] and request.user.role != "SALES":
            return Event.objects.filter(
                id=view.kwargs["pk"], support_contact_id=request.user.id
            ).exists()
        return False
