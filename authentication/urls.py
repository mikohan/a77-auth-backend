from django.contrib import admin
from django.urls import path
from .views import (
    LoginAPIView,
    RegisterView,
    VerifyEmailView,
    PasswordTokenCheckAPIView,
    RequestPasswordResetEmail,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("activate/", VerifyEmailView.as_view(), name="activate"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("reset/", RequestPasswordResetEmail.as_view(), name="reset"),
    path(
        "reset/<str:uidb64>/<str:token>/",
        PasswordTokenCheckAPIView.as_view(),
        name="reset-confirm",
    ),
]
