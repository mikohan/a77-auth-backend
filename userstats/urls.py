from django.urls import path
from .views import ExpensesSummary, IncomeSummary


urlpatterns = [
    path(
        "expense-catogory-summary",
        ExpensesSummary.as_view(),
        name="expense-category-summary",
    ),
    path(
        "income-catogory-summary",
        IncomeSummary.as_view(),
        name="income-category-summary",
    ),
]
