from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.IndexViewdashboard.as_view(),name="dashboard"),
    path('login/', views.User_login.as_view(), name='adminlogin'),
    path('logout/', views.user_logout, name='logout'),
    path('export-csv',views.exportemp,name='exportcsvemp'),
    # path('profile', views.Showuserprofile.as_view(),name="profile"),
    path('adminUsers/create', views.AddAdminUserView.as_view(),name="adminUsersCreate"),
    path('adminUsers/', views.AdminUserListView,name="adminUsersList"),
    path('EmployeUsers/create', views.AddEmployeUserView.as_view(),name="EmployeUsersCreate"),
    path('EmployeUsers/', views.EmployeUserListView,name="EmployeUsersList"),
    path('ResponsableUsers/create', views.AddResponsableUserView.as_view(),name="ResponsableUsersCreate"),
    path('ResponsableUsers/', views.ResponsableUserListView,name="ResponsableUsersList"),
]