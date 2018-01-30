from ShelfieUser.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate

class ExampleAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        # Get the username and password
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed(_('No credentials provided.'))

        credentials = {
            'username': username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))


        return (user, None)  # authentication successful
