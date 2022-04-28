from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name': "first_name",
                'id': "first_name",
                'placeholder': "First Name",
                'class': "form-control",
            }
        ),
        label=''
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name': "last_name",
                'id': "last_name",
                'placeholder': "Last Name",
                'class': "form-control",
            }
        ),
        label=''
    )
    email = forms.EmailField(
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'name': "email",
                'id': "email",
                'placeholder': "Email",
                'class': "form-control",
            }
        ),
        label=''
    )
    username = forms.CharField(
        required=True,
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'name': "username",
                'id': "username",
                'placeholder': "Username",
                'class': "form-control",
            }
        ),
        label=''
    )
    password = forms.CharField(
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'name': "password1",
                'id': "password1",
                'placeholder': "Password",
                'class': "form-control",
            }
        ),
        label=''
    )
    confirm_password = forms.CharField(
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'name': "password2",
                'id': "password2",
                'placeholder': "Confirm Password",
                'class': "form-control",
            }
        ),
        label=''
    )
