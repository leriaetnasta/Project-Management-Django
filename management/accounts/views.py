from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
import csv


def has_group(user, group):
    return user.groups.filter(name=group).exists()


class IndexViewdashboard(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'admins')
    def get(self, request):
        return render(request,"dashboard/indexdashboard.html",{})



class AddAdminUserView(UserPassesTestMixin, View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'admins')
    def get(self,request):
        user_form = UserCreationForm()
        admin_form = AdminForm(request.POST)
        return render(request,'dashboard/admin/registeradmin.html',{'user_form': user_form,'admin_form':admin_form})
    def post(self,request):
        user_form = UserCreationForm(request.POST)
        admin_form = AdminForm(request.POST,request.FILES)

        if user_form.is_valid() and admin_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            group = groups.objects.get(name='employes')
            new_user.groups.add(group)
            group = groups.objects.get(name='admins')
            new_user.groups.add(group)
            new_admin=admin_form.save(commit=False)
            new_admin.user=new_user
            new_admin.is_employe=True
            new_admin.is_admin=True
            new_admin.save()
            
            return redirect("adminUsersList")
        return HttpResponse('Données invalides')
@login_required
def AdminUserListView(request):
        adminUsers=Admin.objects.all() 
        return render(request,"dashboard/admin/listeadmin.html",{'adminUsers':adminUsers})

class AddEmployeUserView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'admins')
    def get(self,request):
        user_form = UserCreationForm()
        emp_form = EmployeForm(request.POST)
        return render(request,'dashboard/employe/registeremploye.html',{'user_form': user_form,'emp_form':emp_form})
    def post(self,request):
        user_form = UserCreationForm(request.POST)
        emp_form = EmployeForm(request.POST,request.FILES)

        if user_form.is_valid() and emp_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            group = Group.objects.get(name='employes')
            new_user.groups.add(group)
            group = Group.objects.get(name='employes')
            new_user.groups.add(group) 
            new_emp=emp_form.save(commit=False)
            new_emp.user=new_user
            new_emp.is_employe=True
             
            new_emp.save()
            return render(request,'dashboard/employe/profile.html',{'new_emp': new_emp})
        return HttpResponse('Données invalides')
@login_required
def EmployeUserListView(request):
        employeUsers=Employe.objects.all() 
        return render(request,"dashboard/employe/Employe_list.html",{'employeUsers':employeUsers})

class AddResponsableUserView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'admins')
    def get(self,request):
        user_form = UserCreationForm()
        resp_form = ResponsableForm(request.POST)
        return render(request,'dashboard/responsable/registerresponsable.html',{'user_form': user_form,'resp_form':resp_form})
    def post(self,request):
        user_form = UserCreationForm(request.POST)
        resp_form = ResponsableForm(request.POST,request.FILES)

        if user_form.is_valid() and resp_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            group = Group.objects.get(name='employes')
            new_user.groups.add(group)
            new_resp=resp_form.save(commit=False)
            new_resp.user=new_user
            new_resp.is_employe=True
            new_resp.is_responsable=True
            new_resp.save()
            return render(request,'dashboard/responsable/profile.html',{'new_user': new_user})
        return HttpResponse('Données invalides')
@login_required
def ResponsableUserListView(request):
        ResponsableUsers=Responsable.objects.all() 
        return render(request,"dashboard/Responsable/listResponsable.html",{'ResponsableUsers':ResponsableUsers})
class User_login(View):
    def get(self,request):
        form = LoginForm(request.POST)
        return render(request, 'dashboard/login.html', {'form': form})
    def post(self,request):
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active and has_group(user,'admins'):
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse("you're not an admin")
            else:
                return HttpResponse('Invalid login')
        return redirect("/")

def user_logout(request):
    logout(request)
    return redirect('/')

def exportemp(request):
    response= HttpResponse(content_type='text/csv')
    writer=csv.writer(response,delimiter=',')
    writer.writerow(['nom','prenom','email','titre','sexe','code eemploye','date de naissance','role','adresse','ville','telephone','cin'])
    for task in Employe.objects.all().values_list('nom','prenom','email','titre','sexe','ce','date_naissance','role','adresse','ville','telephone','cin'):
        writer.writerow(task)
    response['Content-Disposition']= 'attachement ; filename="employe.csv"'
    return response