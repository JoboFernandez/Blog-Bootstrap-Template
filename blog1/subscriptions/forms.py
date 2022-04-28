from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': "email",
                'name': "email",
                'id': "email",
                'placeholder': "Type your email address"
            }
        ),
        label=''
    )

    class Meta:
        model = Subscription
        fields = ['email']