from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

class EmployeeInline(admin.StackedInline):
    model = Employe
    can_delete = False
    verbose_name_plural = 'employes'

class ResponsableInline(admin.StackedInline):
    model = Responsable
    can_delete = False
    verbose_name_plural = 'Responsables'

class AdminInline(admin.StackedInline):
    model = Admin
    can_delete = False
    verbose_name_plural = 'Admins'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,ResponsableInline,AdminInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Employe)
admin.site.register(Admin)
admin.site.register(Responsable)