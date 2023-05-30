import pytest
from .fixtures import *
from rest_framework.test import APIClient
from api.utils import GenerateFaker

@pytest.mark.django_db
def test_sales_user_update_client(sales_user):
    my_client = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    my_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    response = my_client.patch('/clients/1/', {'first_name': 'Thomas'})
    assert response.status_code == 200
    assert b'"first_name":"Thomas"' in response.content