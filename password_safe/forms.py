from django import forms
from .models import Accounts


class UserForm(forms.ModelForm):
    class Meta:
        model = Accounts
        widgets = {
            "password": forms.PasswordInput(),
        }
