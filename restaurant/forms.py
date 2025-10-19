from django import forms
from .models import Meal,OrderTransaction,User

from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d’utilisateur','autocomplete':'off'})
    )
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'id': 'password_id', 'class': 'form-control', 'placeholder': 'Mot de passe'})

    )

    show = forms.BooleanField(
    label='Afficher',
    widget=forms.CheckboxInput(
        attrs={'class': 'show-password'}
    ),
    required=False
)