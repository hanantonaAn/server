from user.models import User
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend

class AuthBackend(object):
    supports_object_permissions = True

    def get_user(self, user_id):
        try:
           return User.objects.get(pk=user_id)
        except User.DoesNotExist:
           return None

    def authenticate(self, request, username, password):

        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username)
            )

        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        else:
            return None