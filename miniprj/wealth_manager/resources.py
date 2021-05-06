from import_export import resources
from .models import Expense, Income

class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expense

class IncomeResource(resources.ModelResource):
    class Meta:
        model = Income