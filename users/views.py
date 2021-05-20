from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from rest_framework import viewsets
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
