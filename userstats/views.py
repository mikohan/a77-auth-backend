from django.shortcuts import render
from rest_framework.views import APIView
from expenses.models import Expense
from income.models import Income
from rest_framework import status, response

import datetime


class ExpensesSummary(APIView):
    def get_category(self, expense):
        return expense.category

    def get_amount_for_category(self, expenses, category):
        expenses = expenses.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount
        return {"amount": str(amount)}

    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=365)

        expenses = Expense.objects.filter(
            owner=request.user, date__gte=str(ayear_ago), date__lte=str(today_date)
        )
        categories = list(set(map(self.get_category, expenses)))

        final = {}

        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expenses, category)
        return response.Response({"category_data": final}, status=status.HTTP_200_OK)


class IncomeSummary(APIView):
    def get_source(self, income):
        return income.source

    def get_amount_for_source(self, incomes, source):
        incomes = incomes.filter(source=source)
        amount = 0

        for income in incomes:
            amount += income.amount
        return {"amount": str(amount)}

    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=365)

        incomes = Income.objects.filter(
            owner=request.user, date__gte=str(ayear_ago), date__lte=str(today_date)
        )
        sources = list(set(map(self.get_source, incomes)))

        final = {}

        for _ in incomes:
            for source in sources:
                final[source] = self.get_amount_for_source(incomes, source)
        return response.Response({"sources_data": final}, status=status.HTTP_200_OK)
