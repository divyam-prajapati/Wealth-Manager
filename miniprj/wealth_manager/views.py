from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
    return render(request, "manager/expense.html", {'nbar': 'expense'})

def income(request): 
    return render(request, "manager/income.html", {'nbar': 'income'})

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

