from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Vous devez entrer un email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="MANAGEMENT",
            is_staff=True,
            is_active=True,
            is_admin=True,
        )
        user.save()

        return user


# https://thinkster.io/tutorials/django-json-api/authentication
class User(AbstractBaseUser):
    ROLE = [
        ("SALES", "SALES"),
        ("SUPPORT", "SUPPORT"),
        ("MANAGEMENT", "MANAGEMENT"),
    ]

    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, choices=ROLE, default=ROLE[1])
    tel = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self.pk}: { self.email } - Role : {self.role}"


class Client(models.Model):
    is_prospect = models.BooleanField(default=True)
    sales_contact = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True, blank=True
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    tel = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=250, blank=True, default="")
    facebook = models.CharField(max_length=100, blank=True, default="")
    twitter = models.CharField(max_length=100, blank=True, default="")
    linkedin = models.CharField(max_length=100, blank=True, default="")
    date_created = models.DateTimeField("Created_Date", auto_now_add=True)
    date_updated = models.DateTimeField("Updated_Date", auto_now=True)

    def __str__(self):
        return f"{self.pk}: { self.first_name } { self.last_name } - is_prospect : {self.is_prospect}"


class Contract(models.Model):
    sales_contact = models.ForeignKey(User, on_delete=models.RESTRICT)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True, blank=True)
    date_created = models.DateTimeField("Created_Date", auto_now_add=True)
    date_updated = models.DateTimeField("Updated_Date", auto_now=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField()
    payement_due = models.DateTimeField("Payement_Date", auto_now=False)

    def __str__(self):
        return (
            f"Contract { self.pk } "
            f"- Client : {self.client.company_name} - {self.client.first_name} {self.client.last_name}"
        )


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True, blank=True)
    contract = models.ForeignKey(
        Contract, on_delete=models.RESTRICT, null=True, blank=True
    )
    support_contact = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True, blank=True
    )
    date_created = models.DateTimeField("Created_Date", auto_now_add=True)
    date_updated = models.DateTimeField("Updated_Date", auto_now=True)
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField("event_date", auto_now_add=False, blank=True)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return (
            f"Event { self.pk} "
            f"- Client : {self.client.company_name} - {self.client.first_name} {self.client.last_name}"
        )
