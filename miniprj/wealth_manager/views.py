from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "manager/dashboard.html", {'nbar': 'home'})

def expense(request): 
    return render(request, "manager/expense.html", {'nbar': 'expense'})

def income(request): 
    return render(request, "manager/income.html", {'nbar': 'income'})

def bankAccount(request): 
    return render(request, "manager/income.html", {'nbar': 'bankAccount'})

def budget(request): 
    return render(request, "manager/income.html", {'nbar': 'budget'})

def savings(request): 
    return render(request, "manager/income.html", {'nbar': 'savings'})

def profile(request): 
    return render(request, "manager/income.html", {'nbar': 'profile'})

def help(request): 
    return render(request, "manager/income.html", {'nbar': 'help'})

def logout(request): 
    return render(request, "manager/income.html", {'nbar': 'logout'})