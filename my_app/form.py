from django import forms
from .models import Article


class ActicleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=[
            "titre",
            "description",
            
        ]
