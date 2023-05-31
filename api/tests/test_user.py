import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.utils import GenerateFaker
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


class AuthViewsTests(APITestCase):

    def setUp(self):
        self.support = GenerateFaker("SUPPORT")
        self.sales = GenerateFaker("SALES")
        self.management = GenerateFaker("MANAGEMENT")

    def test_create_support_user(self):
        url = reverse('signup')
        response = self.client.post(url, self.support.get_group_data(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)

    def test_login_support_user(self):
        user = get_user_model().objects.create(**self.support.get_simplified_group_data())
        u = get_user_model().objects.get(**self.support.get_simplified_group_data())
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post("/api/login/", {'email': u.email, 'password': u.password})

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


    def test_create_sales_user(self):
        url = reverse('signup')
        response = self.client.post(url, self.sales.get_group_data(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)

    def test_create_gestion_user(self):
        url = reverse('signup')
        response = self.client.post(url, self.management.get_group_data(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)