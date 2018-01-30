from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse

from knox.views import LoginView as KnoxLoginView
from ShelfieUser.authentication import ExampleAuthentication


class LoginView(KnoxLoginView):
    authentication_classes = [ExampleAuthentication,]

@api_view(["GET"])
@login_required
def api_home(request):
    data = {
        "Users": api_reverse("UserListAPIView")
    }
    return Response(data)
