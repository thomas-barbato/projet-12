import pytest
from api.models import Client, User, Event, Contract
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from api.utils import GenerateFaker


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return refresh.access_token

@pytest.fixture
def user_support():
    user = GenerateFaker("SUPPORT").get_group_data()
    return user

@pytest.fixture
def sales_user():
    u = GenerateFaker("SALES").get_group_data()
    data = GenerateFaker("")
    user = User.objects.create(**u)
    client = Client.objects.create(**data.get_client())
    Contract.objects.create(sales_contact_id=user.id, client_id=client.id, **data.get_contract())
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client

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
