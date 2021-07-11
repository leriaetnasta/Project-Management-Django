from django.contrib import admin
from django.conf import settings
from .models import *
admin.site.register(Projet)
admin.site.register(Tache)
admin.site.register(RessourceMateriel)
admin.site.register(Category)