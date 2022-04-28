from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(
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
        widget=forms.PasswordInput(
            attrs={
                'name': "password",
                'id': "password",
                'placeholder': "Password",
                'class': "form-control",
            }
        ),
        label=''
    )

