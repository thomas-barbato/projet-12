from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.forms import CustomUserAdminForm
from api.models import Client, Contract, Event, User


class CustomUserAdmin(ModelAdmin):
    model = User
    form = CustomUserAdminForm

    fieldsets = (
        ("Informations de connexion", {"fields": ("email", "password")}),
        (
            "Informations personnelles",
            {"fields": ("first_name", "last_name", "role", "tel")},
        ),
    )

    ordering = ("id",)

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    fields = (
        "first_name",
        "last_name",
        "tel",
        "mobile",
        "email",
        "facebook",
        "twitter",
        "linkedin",
        "company_name",
        "is_prospect",
        "sales_contact",
        "date_created",
        "date_updated",
    )
    readonly_fields = ("date_created", "date_updated")


@admin.register(Contract)
class ContractAdmin(ModelAdmin):
    fields = (
        "client",
        "sales_contact",
        "amount",
        "status",
        "payement_due",
        "date_created",
        "date_updated",
    )
    readonly_fields = ("date_created", "date_updated")


@admin.register(Event)
class EventAdmin(ModelAdmin):
    fields = (
        "client",
        "support_contact",
        "event_date",
        "attendees",
        "notes",
        "date_created",
        "date_updated",
    )
    readonly_fields = ("date_created", "date_updated")
