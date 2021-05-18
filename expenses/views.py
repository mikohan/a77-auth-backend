from expenses.models import Expense
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    queryset = Expense.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Expense.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
