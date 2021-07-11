from accounts.models import *
from django.contrib.auth.models import User
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput,label="le mot de passe")