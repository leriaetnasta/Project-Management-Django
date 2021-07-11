from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields= "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= "__all__"

class TacheForm(forms.ModelForm):
    class Meta:
        model=Tache
        fields= "__all__"

class RessourceForm(forms.ModelForm):
    class Meta:
        model= RessourceMateriel
        fields= "__all__"


