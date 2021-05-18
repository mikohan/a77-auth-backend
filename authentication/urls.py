from django.contrib import admin
from django.urls import path
from .views import LoginAPIView, RegisterView, VerifyEmailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("activate/", VerifyEmailView.as_view(), name="activate"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
