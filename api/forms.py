from django.contrib import admin
from django import forms
from django.forms import PasswordInput

from api.models import User
from api.validators.check_data import CheckPasswordPolicy


class CustomUserAdminForm(forms.ModelForm):

    password = forms.CharField(
        widget=PasswordInput(),
        required=True,
        label="Password:",
        validators=[CheckPasswordPolicy().validate_form],
    )

    class Meta:
        model = User
        fields = (
            'email',
            "first_name",
            "last_name",
            "email",
            "password",
            "tel",
            "role",
            "is_active",
            "is_staff",
            "is_admin"
        )

    def save(self, commit=True):
        user = super(CustomUserAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if self.cleaned_data["role"] == "MANAGEMENT":
            user.is_admin = True
            user.is_staff = True
        user.is_active = True
        user.save()
        return user
