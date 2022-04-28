from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

from ..forms import SignUpForm


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect("/accounts/signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect("/accounts/signup")
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password
                )
                user.save()
                return redirect("/accounts/signin")

        else:
            messages.info(request, "Password confirmation not matching")
            return redirect("/accounts/signup")

    else:
        context = {
            "form": SignUpForm,
        }
        return render(request, "accounts/signup_form.html", context=context)


# class UserCreateView(CreateView):
#     template_name = 'accounts/signup_form.html'
#     form_class = SignUpForm
#     model = User
#     # fields = ['first_name', 'last_name', 'email', 'username', 'password']
#
#     def get_success_url(self):
#         return reverse("accounts:signin")