from django.contrib.auth.backends import ModelBackend

from ..models import User


class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
