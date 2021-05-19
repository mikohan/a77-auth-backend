from rest_framework import serializers
from typing import AnyStr, Dict, OrderedDict

from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import (
    smart_str,
    force_str,
    smart_bytes,
    DjangoUnicodeDecodeError,
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        # email = attrs.get("email", "")
        username = attrs.get("username", "")

        if not username.isalnum():
            raise serializers.ValidationError(
                "The username should only contain alphanumeric characters"
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ("token",)


class LoginAPIViewSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=555, read_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "username", "tokens"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = auth.authenticate(email=email, password=password)
        print(dir(user))

        if not user:
            raise AuthenticationFailed("Inalid credentials try again")

        if not user.is_active:
            raise AuthenticationFailed("Account disabled contact admin")
        if not user.is_verified:
            raise AuthenticationFailed("Account is not activated")

        return {"email": user.email, "username": user.username, "tokens": user.tokens}


class ResetPasswordEmailResetSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=6)

    class Meta:
        fields = ["email"]


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=255, write_only=True)
    uidb64 = serializers.CharField(min_length=1)
    token = serializers.CharField(min_length=1)

    class Meta:
        fields = ["password", "token", "uidb64"]

    def validate(self, attrs):
        try:
            pass
        except Exception as e:
            pass
