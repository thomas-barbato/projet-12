from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.models import User, Event, Contract, Client


@admin.register(User)
class UserAdmin(ModelAdmin):
    fields = (
        "first_name",
        "last_name",
        "email",
        "tel",
        "role",
        "is_active",
        "is_staff",
        "is_admin"
    )


@admin.register(Event)
class EventtAdmin(ModelAdmin):
    fields = (
        "first_name",
        "last_name",
        "tel",
        "mobile",
        "email",
        "facebook",
        "twitter",
        "linkedin",
        "company",
        "is_prospect",
        "date_created",
        "date_updated",
    )


@admin.register(Contract)
class ContractAdmin(ModelAdmin):
    fields = (
        "client",
        "sales_contact",
        "status",
        "amount",
        "payement_due",
        "date_created",
        "date_updated",
    )


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    fields = (
        "client",
        "support_contact",
        "event_date",
        "attendees",
        "notes",
        "date_created",
        "date_updated",
    )
