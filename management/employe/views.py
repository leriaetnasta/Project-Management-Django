from Operations.forms import *
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required

def has_group(user, group):
    return user.groups.filter(name=group).exists()

# Create your views here.
class IndexhomeView(View):
    def get(self, request):
        return render(request,"interfaceemp/index.html",{})

class ProjetListView(View):
    def get(self,request):
        projects=Projet.objects.all()
        return render(request,"interfaceemp/projetlist.html",{'projects':projects})

class TacheListView(View):
    def get(self,request):
        taches=Tache.objects.all()
        return render(request,"interfaceemp/tachelist.html",{'taches':taches})

class emp_login(View):
    def get(self,request):
        form = LoginForm(request.POST)
        return render(request, 'interfaceemp/login.html', {'form': form})
    def post(self,request):
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active :
                    login(request, user)
                    if has_group(user,'admins') :
                        return redirect('dashboard')
                    elif has_group(user,'responsables') :
                        return redirect('home')
                    else:
                        return redirect('homeview')
                else:
                    return HttpResponse("you're not an emloye")
            else:
                return HttpResponse('Invalid login')
        return redirect("/")

def user_logout(request):
    logout(request)
    return redirect('/')