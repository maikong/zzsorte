from django import forms
from .models import LuckyNumber
from django.contrib.auth.models import User

class LuckyNumberaForm(forms.ModelForm):
    class Meta:
        model = LuckyNumber
        fields = ['email', 'campaign', 'origin']
        widgets = {
            'campaign': forms.Select(attrs={'class': 'form-control form-select', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'origin': forms.Select(attrs={'class': 'form-control form-select', }),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'required'
        }),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': 'required'
        }),
        label='Password'
    )