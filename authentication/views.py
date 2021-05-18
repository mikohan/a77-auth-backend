from authentication.models import User
from django.shortcuts import render
from rest_framework import generics, status

from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


"""
Need to replace site url for activation email to frontend site
"""


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        print(user)
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data["email"])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse("activate")
        absUrl = "http://" + current_site + relativeLink + "?token=" + str(token)
        email_body = f"""
        Hi {user.username} Use link below to activate your account \n
        {absUrl} 
        """
        data = {
            "email_recepient": user.email,
            "email_body": email_body,
            "email_subject": f"Activate your account at {current_site}",
        }
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmailView(generics.CreateAPIView):
    def get(self, request):
        token = request.GET.get("token")
