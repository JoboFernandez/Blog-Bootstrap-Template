from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User, auth

from ..forms import SignInForm


def signin(request):
    context = {
        "form": SignInForm,
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("/accounts/signin")
    else:
        return render(request, 'accounts/signin_form.html', context)
