from django.urls import path
from . import views
from .views import ChartData

urlpatterns = [
    path("", views.index, name="index"),
    path("Expense/", views.expense, name="expense"),
    path("Income/", views.income, name="income"),
    path("BankAccount/", views.bankAccount, name="bankAccount"),
    path("Budget/", views.budget, name="budget"),
    path("Savings/", views.savings, name="savings"),
    path("Profile/", views.profile, name="profile"),
    path("Help/", views.help, name="help"),
    path("Login/", views.login_view, name="login"),
    path("Logout/", views.logout_view, name="logout"),
    path("Signup/", views.signup, name="signup"),
    path('api/chart/expense_data/', ChartData.as_view(), name="api-chart-expense-data"),
    path('Expense/<int:object_id>/', views.delete_expense, name="delete-object"),
]