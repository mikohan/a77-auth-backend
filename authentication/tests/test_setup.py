from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    user_data = {
        "email": "email@gamil.com",
        "username": "email",
        "password": "password1234",
    }

    def setUp(self) -> None:
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
