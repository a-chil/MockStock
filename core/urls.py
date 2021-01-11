"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_register import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("register/", user_views.register, name="register"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="user_register/login.html")
    ),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="user_register/reset_pass.html"
        ),
    ),
    path(
        "reset_password_sent",
        auth_views.PasswordResetDoneView.as_view(
            template_name="user_register/reset_pass_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset_password/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="user_register/reset_pass_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="user_register/reset_pass_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("logout/", auth_views.LogoutView.as_view()),
]
