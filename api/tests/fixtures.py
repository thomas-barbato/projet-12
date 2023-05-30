import pytest
from api.models import Client, User, Event, Contract
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from api.utils import GenerateFaker


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return refresh.access_token

@pytest.fixture
def sales_user():
    u = GenerateFaker("SALES").get_group_data()
    c = GenerateFaker().get_client()
    user = User(
        **u
    )
    client = Client(
        **c
    )
    user.save()
    client.save()
    return user


@pytest.fixture
def management_user():
    data = GenerateFaker("MANAGEMENT").get_group_data()
    user = User.objects.create(
        **data
    )
    return user


@pytest.fixture
def support_user():
    data = GenerateFaker("SUPPORT").get_group_data()
    user = User.objects.create(
        **data
    )
    return user
