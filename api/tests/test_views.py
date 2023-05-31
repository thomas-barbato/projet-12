import pytest
from .fixtures import *
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.utils import GenerateFaker

@pytest.mark.django_db
def test_get_contracts(sales_user):
    url = "/api/contracts/"
    response = sales_user.get(url)
    data = response.data
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_contracts_details(sales_user):
    url = "/api/contracts/2/"
    response = sales_user.get(url)
    data = response.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_patch_contracts_details(sales_user):
    url = "/api/contracts/2/"
    response = sales_user.patch(url, {"amount": "15.0"})
    data = response.data
    assert response.status_code == status.HTTP_200_OK