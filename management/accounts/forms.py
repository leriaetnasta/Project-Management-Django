from .models import *
from django.contrib.auth.models import User
from django import forms

        
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = "__all__"
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput,label="le mot de passe")
