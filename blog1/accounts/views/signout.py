from django.shortcuts import redirect
from django.contrib.auth.models import auth


def signout(request):
    auth.logout(request)
    return redirect("/")