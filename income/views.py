from income.permissions import IsOwner
from income.models import Income
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IncomeSerializer
from rest_framework.permissions import IsAuthenticated


class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    queryset = Income.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Income.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
