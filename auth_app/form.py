from  django import forms
from django.contrib.auth.forms import UserCreationForm


class AuthUser(UserCreationForm):
    password1 = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )

    password2 = forms.CharField(
        label="password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
        strip=False,
    )
#class meta pour personnaliser les chants du formulaire
    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields +("password1","password2")