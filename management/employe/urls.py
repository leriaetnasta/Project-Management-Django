from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexhomeView.as_view(),name='homeview'),
    path('login/', views.emp_login.as_view(), name='employelogin'),
    path('logout/', views.user_logout, name='emplogout'),
    path('projets/',views.ProjetListView.as_view(),name='empprojectList'),
    path('taches/',views.TacheListView.as_view(),name='emptacheList'),
    ]