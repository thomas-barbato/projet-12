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
        "date_created",
        "date_updated",
    )
    readonly_fields = ('date_created', 'date_updated')


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
    readonly_fields = ('date_created',)

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
    readonly_fields = ('date_created', 'date_updated')
