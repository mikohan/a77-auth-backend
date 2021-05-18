from authentication.models import User
from django.shortcuts import render
from rest_framework import generics, status, views

from .serializers import (
    EmailVerificationSerializer,
    RegisterSerializer,
    LoginAPIViewSerializer,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


"""
Need to replace site url for activation email to frontend site
"""


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
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


class VerifyEmailView(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        "token",
        in_=openapi.IN_QUERY,
        description="Description",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):

        token = request.GET.get("token")
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        print(payload)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            print(payload, user)

            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                {"email": "Successfully activated"}, status=status.HTTP_201_CREATED
            )

        except jwt.ExpiredSignatureError as indentifier:
            return Response(
                {"error": "Activation link Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.DecodeError as indentifier:
            return Response(
                {"error": "Invalid token request new one"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginAPIViewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
