from django.urls import path
from .views import ExpensesSummary


urlpatterns = [
    path(
        "expense-catogory-summary",
        ExpensesSummary.as_view(),
        name="expense-category-summary",
    )
]
