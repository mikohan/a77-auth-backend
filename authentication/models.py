from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if username in None:
            raise TypeError("Users sould have a useername")
        if email in None:
            raise TypeError("Users sould have a email")

        user = self.model(username=username, email=self.normalize_email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if password in None:
            raise TypeError("Password should not be none")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_stuff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionMixin):
    username = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    id_verified = models.BooleanField(default=False)
    id_active = models.BooleanField(default=True)
    id_stuff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ""
