from django.contrib import admin
from django import forms
from api.models import User

class CustomUserAdminForm(forms.ModelForm):
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
        # Save the provided password in hashed format
        user = super(CustomUserAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            if user.role == "MANAGEMENT":
                user.is_admin = True
            user.save()
        return user