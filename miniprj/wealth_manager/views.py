from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Expense
from .models import Income

from wealth_manager.models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "manager/dashboard.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "manager/login.html", {
                "message": "Invalid Credentials!",
            })
    return render(request, "manager/login.html")

def logout_view(request): 
    logout(request)
    return render(request, "manager/login.html", {
        "message": "Logged Out!",
    })

def signup(request): 
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(
            username, email, password, 
            first_name = fname,
            last_name = lname,
        )
        user.save()
        return render(request, "manager/login.html", {
                "message": "User Created",
            })

    return render(request, "manager/signup.html") 

def expense(request): 
    if request.method == "POST":
        amount = request.POST["amount"]
        date = request.POST["date"]
        category = request.POST["category"]
        description = request.POST["description"]
        e = Expense(expenseAmount = amount, expenseDate = date, expenseCategory = category, expenseDescription = description )
        if e is not None: 
            e.save()
            return render(request, "manager/expense.html", {
                    "expense": Expense.objects.all(),
                    'nbar': 'expense',
                    "message": "Expense Added Successfully",
                    "status": "1"
            })
        else: 
            return render(request, "manager/expense.html", {
                    "expense": Expense.objects.all(),
                    'nbar': 'expense',
                    "message": "Error Unsuccessfully!",
                    "status": "0"
            })

    return render(request, "manager/expense.html", {
        "expense": Expense.objects.all(),
        'nbar': 'expense'
    })

def income(request): 
    return render(request, "manager/income.html", {
        "income": Income.objects.all(),    
        'nbar': 'income',
    })

def bankAccount(request): 
    return render(request, "manager/bankAccount.html", {'nbar': 'bankAccount'})

def budget(request): 
    return render(request, "manager/budget.html", {'nbar': 'budget'})

def savings(request): 
    return render(request, "manager/savings.html", {'nbar': 'savings'})

def profile(request): 
    return render(request, "manager/profile.html", {'nbar': 'profile'})

def help(request): 
    return render(request, "manager/help.html", {'nbar': 'help'})

def delete_expense(request, object_id):
    object = Expense.objects.get(id = object_id) 
    object.delete()     
    return render(request, "manager/expense.html", {
        "message": "Expense Deleted Successfully",
        'status': '0',
        "expense": Expense.objects.all(),
        'nbar': 'expense',
    })

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        data = {
            "data": Expense.objects.values(),#PAss INTEGER values of data in array
        }
        
        return Response(data)



