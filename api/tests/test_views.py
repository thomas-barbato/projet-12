import pytest

from api.models import User


@pytest.mark.django_db
def test_user_create():
  User.objects.create(
      email="management56@email.fr",
      password="Thomas404*",
      role="MANAGEMENT",
      tel="07.71.93.73.70",
  )
  assert User.objects.count() == 1


