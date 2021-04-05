from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Expense/", views.expense, name="expense"),
    path("Income/", views.income, name="income"),
    path("BankAccount/", views.bankAccount, name="bankAccount"),
    path("Budget/", views.budget, name="budget"),
    path("Savings/", views.savings, name="savings"),
    path("Profile/", views.profile, name="profile"),
    path("Help/", views.help, name="help"),
    path("Logout/", views.logout, name="logout"),
]