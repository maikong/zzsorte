from django import forms
from .models import LuckyNumber

class LuckyNumberaForm(forms.ModelForm):
    class Meta:
        model = LuckyNumber
        fields = ['email', 'origin']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'origin': forms.Select(attrs={'class': 'form-control form-select', }),
        }