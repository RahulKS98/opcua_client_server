from django import forms
from django.core.validators import EmailValidator

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password",required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class registerForm(forms.Form):
    username = forms.CharField(label="Username",required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password",required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class nodeForm(forms.Form):
    CHOICES = (
        ('VVB001', 'VVB001'),
        ('O5D100', 'O5D100'),
    )
    dropdown = forms.ChoiceField(label="Select Node",choices=CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-select mt-2'}))