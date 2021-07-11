from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from accounts.forms import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import Group
from .utils import get_plot
import pandas as pd
from django.db.models import Avg, Q
import csv
# Create your views here.
def has_group(user, group):
    return user.groups.filter(name=group).exists()

class IndexView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self, request):
        return render(request,"index.html",{})

class ProjetView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        form=ProjectForm()
        return render(request,"Projects/Project_form.html",{'form':form})
    def post(self,request):
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
        return redirect("projectList")

class ProjetListView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        projects=Projet.objects.all()
        return render(request,"Projects/Project_List.html",{'projects':projects})

class ProjetUpdateView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        project=Projet.objects.get(id=idp)
        form=ProjectForm(instance=project)
        return render(request,"Projects/Project_form.html",{'form':form})
    def post(self,request,idp):
        project=Projet.objects.get(id=idp)
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
           form.save()
        return redirect("projectList")

class ProjetDeleteView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        return render(request,"Projects/delete_project_form.html",{})
    def post(self,request,idp):
        project=Projet.objects.get(id=idp)
        project.delete()
        return redirect("projectList")

class ProjetDetailsView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        project=Projet.objects.get(id=idp)
        return render(request,"Projects/project_details.html",{'project':project})

class CategoryListView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        categories=Category.objects.all()
        return render(request,"Categories/category_list.html",{'categories':categories})

class CategoryView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        form=CategoryForm()
        return render(request,"Categories/Category_form.html",{'form':form})
    def post(self,request):
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
        return redirect("categoryList")

class CategoryUpdateView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        category=Category.objects.get(id=idp)
        form=CategoryForm(instance=category)
        return render(request,"Categories/category_form.html",{'form':form})
    def post(self,request,idp):
        category=Category.objects.get(id=idp)
        form=CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
           form.save()
        return redirect("categoryList")

class CategoryDeleteView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        return render(request,"Categories/delete_category_form.html",{})
    def post(self,request,idp):
        category=Category.objects.get(id=idp)
        category.delete()
        return redirect("categoryList")

class CategoryDetailsView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        category=Category.objects.get(id=idp)
        return render(request,"Categories/category_details.html",{'category':category})

class TacheView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        form=TacheForm()
        return render(request,"Tasks/tache_form.html",{'form':form})
    def post(self,request):
        form=TacheForm(request.POST,request.FILES)
        if form.is_valid():
           form.save(commit=True)
        return redirect("tacheList")

class TacheListView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        taches=Tache.objects.all()
        return render(request,"Tasks/tache_list.html",{'taches':taches})

# class TacheGanttView(View):
#     def get(self,request):
#         import plotly.graph_objects as go
#         fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#         fig.write_html('first_figure.html', auto_open=True)

class TacheUpdateView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        tache=Tache.objects.get(id=idp)
        form=TacheForm(instance=tache)
        return render(request,"Tasks/Tache_form.html",{'form':form})
    def post(self,request,idp):
        tache=Tache.objects.get(id=idp)
        form=TacheForm(request.POST,request.FILES,instance=tache)
        if form.is_valid():
           form.save()
        return redirect("tacheList")

class TacheDeleteView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        return render(request,"Tasks/delete_tache_form.html",{})
    def post(self,request,idp):
        tache=Tache.objects.get(id=idp)
        tache.delete()
        return redirect("tacheList")

class TacheDetailsView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        tache=Tache.objects.get(id=idp)
        return render(request,"Tasks/Tache_details.html",{'tache':tache})

class RessourceView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        form=RessourceForm()
        return render(request,"Ressources/Ressource_form.html",{'form':form})
    def post(self,request):
        form=RessourceForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
        return redirect("ressourceList")

class RessourceListView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        ressources=RessourceMateriel.objects.all()
        return render(request,"Ressources/Ressource_list.html",{'ressources':ressources})

class RessourceUpdateView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        Ressource=RessourceMateriel.objects.get(id=idp)
        form=RessourceForm(instance=Ressource)
        return render(request,"Ressources/Ressource_form.html",{'form':form})
    def post(self,request,idp):
        Ressource=RessourceMateriel.objects.get(id=idp)
        form=RessourceForm(request.POST,request.FILES,instance=Ressource)
        if form.is_valid():
           form.save()
        return redirect("ressourceList")

class RessourceDeleteView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        return render(request,"Ressources/delete_Ressource_form.html",{})
    def post(self,request,idp):
        Ressource=RessourceMateriel.objects.get(id=idp)
        Ressource.delete()
        return redirect("ressourceList")

class RessourceDetailsView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        Ressource=RessourceMateriel.objects.get(id=idp)
        return render(request,"Ressources/Ressource_details.html",{'Ressource':Ressource})

class EmployeView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        user_form = UserCreationForm()
        emp_form = EmployeForm(request.POST)
        return render(request,"Employes/employe_form.html",{'user_form': user_form,'emp_form':emp_form})
    def post(self,request):
        user_form = UserCreationForm(request.POST)
        emp_form = EmployeForm(request.POST,request.FILES)

        if user_form.is_valid() and emp_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            new_emp=emp_form.save(commit=False)
            new_emp.user=new_user
            new_emp.is_employe=True
            new_emp.is_responsable=True
            group = Group.objects.get(name='employes')
            new_user.groups.add(group) 
            new_emp.save()
            return redirect("employeList")
        return HttpResponse('Données invalides')

class EmployeListView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        Employes=Employe.objects.all()
        return render(request,"Employes/Employe_list.html",{'Employes':Employes})

# class EmployeView(View):
#     def get(self,request):
#         form=EmployeForm()
#         return render(request,"Employes/employe_form.html",{'form':form})
#     def post(self,request):
#         form=EmployeForm(request.POST,request.FILES)
#         if form.is_valid():
#            form.save()
#         return redirect("employeList")

class EmployeUpdateView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        employe=Employe.objects.get(id=idp)
        emp_form = EmployeForm(instance=employe)
        return render(request,"Employes/employe_form.html",{'emp_form':emp_form})
    def post(self,request,idp):
        employe=Employe.objects.get(id=idp)
        emp_form=EmployeForm(request.POST,request.FILES,instance=employe)
        if emp_form.is_valid():
            emp_form.save()
            return redirect("employeList")
        return HttpResponse('Données invalides')

class EmployeDeleteView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        return render(request,"Employes/delete_Employe_form.html",{})
    def post(self,request,idp):
        employe=Employe.objects.get(id=idp)
        employe.user.delete()
        employe.delete()
        return redirect("employeList")

class EmployeDetailsView(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request,idp):
        employe=Employe.objects.get(id=idp)
        return render(request,"Employes/Employe_details.html",{'employe':employe})

class User_login(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active and has_group(user,'responsables'):
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        return redirect("home")
        
def userlogout(request):
    logout(request)
    return redirect('/')

       
def graph_view(request):
    qs=Tache.objects.all()
    for q in qs:
        x=[x.nom for x in qs]
        y=[y.duration for y in qs]
        chart=get_plot(x,y)
    
    return render(request,"tasks/graph.html",{'chart':chart})

    
def exporttask(request):
    response= HttpResponse(content_type='text/csv')
    writer=csv.writer(response,delimiter=',')
    writer.writerow(['nom','date de debut','date de fin','la duration','description','status'])
    for task in Tache.objects.all().values_list('nom','debut','fin','duration','desc','status'):
        writer.writerow(task)
    response['Content-Disposition']= 'attachement ; filename="task.csv"'
    return response



class Projetrechercher(UserPassesTestMixin,View):
    def test_func(self):
        qs=self.request.user
        return has_group(qs,'responsables')
    def get(self,request):
        projet=Projet.objects.filter(Q(titre=request.POST.get("cle")))
        return render(request,"Projects/Project_List.html",{'projet':projet})
