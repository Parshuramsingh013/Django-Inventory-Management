from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views

###
from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout_view(request):
    logout(request)
    return render(request, 'inventory/logout.html')
### 


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("add-item/", AddItem.as_view(), name="add-item"),
    path("edit-item/<int:pk>", EditItem.as_view(), name="edit-item"),
    path("delete-item/<int:pk>", DeleteItem.as_view(), name="delete-item"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name = 'inventory/login.html'), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(template_name='inventory/logout.html'), extra_context={'allow_get': True},name="logout"),
    path("logout/", logout_view, name="logout"),
]