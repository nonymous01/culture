from  django import forms
from django.contrib.auth.forms import UserCreationForm


class AuthUser(UserCreationForm):
    email = forms.EmailField(
        label="email",
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'email'}),
        #help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )

    password2 = forms.CharField(
        label="password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )
#class meta pour personnaliser les chants du formulaire
    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields +("password1","password2")