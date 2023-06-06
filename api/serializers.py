"""import """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Client, Event, Contract
from .validators.check_data import CheckPasswordPolicy


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ("id","email", "password", "password2", "first_name", "last_name", "tel", "role")
        read_only_fields = ("id",)

    def validate(self, attrs):
        CheckPasswordPolicy().validate(
            password=attrs["password"], password2=attrs["password2"]
        )
        return super().validate(attrs)

    def create(self, validated_data):
        user = User(
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            tel=self.validated_data["tel"],
            role=self.validated_data["role"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()

        return user


class MyTokenObtainSerializer(TokenObtainSerializer):
    username_field = User.USERNAME_FIELD

    class Meta:
        model = User
        fields = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super(MyTokenObtainSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.EmailField()
        self.fields["password"] = serializers.CharField()

    def validate(self, attrs):
        self.user = User.objects.filter(email=attrs[self.username_field]).first()

        if not self.user:
            raise serializers.ValidationError("The user is not valid.")

        if self.user:
            if not self.user.check_password(attrs["password"]):
                raise serializers.ValidationError("Incorrect credentials.")
        if self.user is None or not self.user.is_active:
            raise serializers.ValidationError(
                "No active account found with the given credentials"
            )

        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplementedError(
            "Must implement `get_token` method for `MyTokenObtainSerializer` subclasses"
        )


class MyTokenObtainPairSerializer(MyTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data


class LoginUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ["id",
                  "sales_contact_id",
                  "client_id",
                  "date_created",
                  "date_updated",
                  "status",
                  "amount",
                  "payement_due",
                  ]
        read_only_fields = ("id",)


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id",
                  "is_prospect",
                  "first_name",
                  "last_name",
                  "tel",
                  "mobile",
                  "email",
                  "company_name",
                  "facebook",
                  "twitter",
                  "linkedin",
                  ]
        read_only_fields = ("id",)

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            "id",
            "date_created",
            "date_updated",
            "attendees",
            "event_date",
            "notes",
            "client",
            "support_contact",
            "contract",
        ]
        read_only_fields = ("id",)