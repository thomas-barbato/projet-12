import os

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (AbstractUser, BaseUserManager,
                                        UserManager)
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")


class Role(models.Model):
    role_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, last_name=None):
        if not email:
            raise ValueError("Vous devez entrer une adresse email.")

        users = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        users.set_password(password)
        users.save(user=self._db)
        return users

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email,
                                password=password,
                                **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_admin = True

        user.save()
        return user


# https://thinkster.io/tutorials/django-json-api/authentication
class User(AbstractBaseUser):

    ROLE = [('SALES', 'SALES'),
            ('SUPPORT', 'SUPPORT'),
            ('MANAGEMENT', 'MANAGEMENT')
            ]

    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, choices=ROLE, default=ROLE[2])
    tel = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.pk}: { self.first_name } { self.last_name } - Role : {self.role}'


class Client(models.Model):
    is_prospect = models.BooleanField(default=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    tel = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=250)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    date_created = models.DateTimeField("Created_Date", auto_now_add=True)
    date_updated = models.DateTimeField("Updated_Date", auto_now_add=True)

    def __str__(self):
        return f'{self.pk}: { self.first_name } { self.last_name } - is_prospect : {self.is_prospect}'


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True, blank=True)
    date_created = models.DateTimeField("Created_Date", auto_now_add=True)
    date_updated = models.DateTimeField("Updated_Date", auto_now_add=True)
    support_contact = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField("event_date", auto_now_add=False)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return f'{ self.client }'


class Contract(models.Model):
    sales_contact = models.ForeignKey(User, on_delete=models.RESTRICT)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True, blank=True)
    date_created = models.DateTimeField("Created_Date", auto_now_add=True)
    date_updated = models.DateTimeField("Updated_Date", auto_now_add=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField()
    payement_due = models.DateTimeField("Payement_Date", auto_now_add=False)

    def __str__(self):
        return f'{ self.client }'

