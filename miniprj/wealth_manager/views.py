from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .resources import ExpenseResource, IncomeResource
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from django.core import serializers
from .models import Expense, Income, property, gold, fd, ppf, Events, EventsExpense

from wealth_manager.models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "manager/dashboard.html",{
        "e": Expense.objects.values('user').annotate(Sum('expenseAmount')),
        "i": Income.objects.values('user').annotate(Sum('incomeAmount')),
        'a': [property.objects.values('user').annotate(Sum('bamt')),
            gold.objects.values('user').annotate(Sum('bamt')),
            fd.objects.values('user').annotate(Sum('samt')),
            ppf.objects.values('user').annotate(Sum('samt')),],
    })

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

# def forgot(request):
#     return render(request, "manager/forgot.html") filter

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
        user = request.POST["user"]
        e = Expense(expenseAmount = amount, expenseDate = date, expenseCategory = category, expenseDescription = description, user = user)
        if e is not None: 
            e.save()
            return render(request, "manager/expense.html", {
                    "expense": Expense.objects.all().order_by('-expenseDate'),
                    'nbar': 'expense',
                    "message": "Expense Added Successfully",
                    "status": "1"
            })
        else: 
            return render(request, "manager/expense.html", {
                    "expense": Expense.objects.all().order_by('-expenseDate'),
                    'nbar': 'expense',
                    "message": "Error Unsuccessfully!",
                    "status": "0"
            })

    return render(request, "manager/expense.html", {
        "expense": Expense.objects.all().order_by('-expenseDate'),
        'nbar': 'expense'
    })

def income(request): 
    if request.method == "POST":
        amount = request.POST["amount"]
        date = request.POST["date"]
        category = request.POST["category"]
        description = request.POST["description"]
        user = request.POST["user"]
        i = Income(incomeAmount = amount, incomeDate = date, incomeCategory = category, incomeDescription = description, user = user )
        if i is not None: 
            i.save()
            return render(request, "manager/income.html", {
                    "income": Income.objects.all().order_by('-incomeDate'),
                    'nbar': 'income',
                    "message": "Income Added Successfully",
                    "status": "1"
            })
        else: 
            return render(request, "manager/income.html", {
                    "income": Income.objects.all().order_by('-incomeDate'),
                    'nbar': 'income',
                    "message": "Error Unsuccessfully!",
                    "status": "0"
            })

    return render(request, "manager/income.html", {
        "income": Income.objects.all().order_by('-incomeDate'),    
        'nbar': 'income',
    })


def assets(request):
    return render(request, "manager/assets.html", {
        'nbar': 'assets',
        "property": property.objects.all().order_by('-date'),
        "gold": gold.objects.all().order_by('-date'),
        "fd": fd.objects.all().order_by('-date'),
        "ppf": ppf.objects.all().order_by('-date'),
        "p": property.objects.values('user').annotate(Sum('bamt')),
        "m": gold.objects.values('user').annotate(Sum('bamt')),
        "f": fd.objects.values('user').annotate(Sum('samt')),
        "pp": ppf.objects.values('user').annotate(Sum('samt')),
    })

def assetsPr(request): 
    if request.method == "POST":
        sqft = request.POST["sqft"]
        date = request.POST["date"]
        bvalue = request.POST["bvalue"]
        description = request.POST["description"]
        user = request.POST["user"]
        i = property(sqft = sqft,date = date,bamt = bvalue,des = description, user = user)
        i.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "Property Added Successfully",
                "status": "1"
        })

    return render(request, "manager/assets.html", {
        'nbar': 'assets',
        "property": property.objects.all().order_by('-date'),
        "gold": gold.objects.all().order_by('-date'),
        "fd": fd.objects.all().order_by('-date'),
        "ppf": ppf.objects.all().order_by('-date'),
        "p": property.objects.values('user').annotate(Sum('bamt')),
        "m": gold.objects.values('user').annotate(Sum('bamt')),
        "f": fd.objects.values('user').annotate(Sum('samt')),
        "pp": ppf.objects.values('user').annotate(Sum('samt')),
    })

def assetsPrE(request, object_id): 
    object = property.objects.get(id = object_id)
    if request.method == "POST":
        object.sqft = request.POST["sqft"]
        object.date = request.POST["date"]
        object.bvalue = request.POST["bvalue"]
        object.description = request.POST["description"]
        object.cpsqft = request.POST["cpsqft"]
        object.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "Property Edited Successfully",
                "status": "1"
        })
    else:
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                'form_data_p': object,
                "pdate": str(object.date)
        })


def assetsPrD(request, object_id):
    object = property.objects.get(id = object_id) 
    object.delete()     
    return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "Property Deleted Successfully",
                "status": "0"
        })
        
def assetsM(request): 
    if request.method == "POST":
        gms = request.POST["gms"]
        date = request.POST["date"]
        type = request.POST["type"]
        bvalue = request.POST["bvalue"]
        description = request.POST["gdescription"]
        user = request.POST["user"]
        g = gold(gms = gms,date = date,type = type,bamt = bvalue,des = description, user = user)
        g.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "Gold Added Successfully",
                "status": "1"
        })

    return render(request, "manager/assets.html", {
        'nbar': 'assets',
        "property": property.objects.all().order_by('-date'),
        "gold": gold.objects.all().order_by('-date'),
        "fd": fd.objects.all().order_by('-date'),
        "ppf": ppf.objects.all().order_by('-date'),
    })

def assetsME(request, object_id): 
    object = gold.objects.get(id = object_id)
    if request.method == "POST":
        object.gms = request.POST["gms"]
        object.date = request.POST["date"]
        object.bamt = request.POST["bvalue"]
        object.type = request.POST["type"]
        object.des = request.POST["gdescription"]
        object.cpm = request.POST["cpm"]
        object.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "Edited Successfully",
                "status": "1"
        })
    else:
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                'form_data_m': object,
                "gdate": str(object.date)
        })


def assetsMD(request, object_id):
    object = gold.objects.get(id = object_id) 
    object.delete()     
    return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "Deleted Successfully",
                "status": "0"
        })

def assetsFd(request): 
    if request.method == "POST":
        samt = request.POST["samt"]
        date = request.POST["date"]
        int = request.POST["int"]
        description = request.POST["description"]
        user = request.POST["user"]
        f = fd(samt = samt,date = date,int = int,des = description, user = user)
        f.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "FD Added Successfully",
                "status": "1"
        })

    return render(request, "manager/assets.html", {
        'nbar': 'assets',
        "property": property.objects.all().order_by('-date'),
        "gold": gold.objects.all().order_by('-date'),
        "fd": fd.objects.all().order_by('-date'),
        "ppf": ppf.objects.all().order_by('-date'),
        "p": property.objects.values('user').annotate(Sum('bamt')),
        "m": gold.objects.values('user').annotate(Sum('bamt')),
        "f": fd.objects.values('user').annotate(Sum('samt')),
        "pp": ppf.objects.values('user').annotate(Sum('samt')),
    })

def assetsFdE(request, object_id): 
    object = fd.objects.get(id = object_id)
    if request.method == "POST":
        object.samt = request.POST["samt"]
        object.date = request.POST["date"]
        object.int = request.POST["int"]
        object.des = request.POST["description"]
        object.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all(),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "FD Edited Successfully",
                "status": "1"
        })
    else:
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                'form_data_f': object,
                "fdate": str(object.date)
        })


def assetsFdD(request, object_id):
    object = fd.objects.get(id = object_id) 
    object.delete()     
    return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "FD Deleted Successfully",
                "status": "0"
        })

def assetsPpf(request): 
    if request.method == "POST":
        samt = request.POST["samt"]
        date = request.POST["date"]
        int = request.POST["int"]
        description = request.POST["description"]
        user = request.POST["user"]
        p = ppf(samt = samt,date = date,int = int,des = description, user = user)
        p.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "PPF Added Successfully",
                "status": "1"
        })

    return render(request, "manager/assets.html", {
        'nbar': 'assets',
        "property": property.objects.all().order_by('-date'),
        "gold": gold.objects.all().order_by('-date'),
        "fd": fd.objects.all().order_by('-date'),
        "ppf": ppf.objects.all().order_by('-date'),
        "p": property.objects.values('user').annotate(Sum('bamt')),
        "m": gold.objects.values('user').annotate(Sum('bamt')),
        "f": fd.objects.values('user').annotate(Sum('samt')),
        "pp": ppf.objects.values('user').annotate(Sum('samt')),
    })

def assetsPpE(request, object_id): 
    object = ppf.objects.get(id = object_id)
    if request.method == "POST":
        object.samt = request.POST["samt"]
        object.date = request.POST["date"]
        object.int = request.POST["int"]
        object.des = request.POST["description"]
        object.save()
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "PPF Edited Successfully",
                "status": "1"
        })
    else:
        return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                'nbar': 'assets',
                'form_data_pp': object,
                "ppdate": str(object.date),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
        })


def assetsPpD(request, object_id):
    object = ppf.objects.get(id = object_id) 
    object.delete()     
    return render(request, "manager/assets.html", {
                "property": property.objects.all().order_by('-date'),
                "gold": gold.objects.all().order_by('-date'),
                "fd": fd.objects.all().order_by('-date'),
                "ppf": ppf.objects.all().order_by('-date'),
                "p": property.objects.values('user').annotate(Sum('bamt')),
                "m": gold.objects.values('user').annotate(Sum('bamt')),
                "f": fd.objects.values('user').annotate(Sum('samt')),
                "pp": ppf.objects.values('user').annotate(Sum('samt')),
                'nbar': 'assets',
                "message": "PPF Deleted Successfully",
                "status": "0"
        })

def events(request): 
    
    if request.method == "POST":
        etitle = request.POST["title"]
        eamount = request.POST["amount"]
        edate = request.POST["date"]
        edescription = request.POST["description"]
        user = request.POST["user"]
        e = Events(eamount = eamount ,edate = edate, etitle = etitle, edescription = edescription, user = user )
        if e is not None: 
            e.save()
            return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    'nbar': 'Events',
                    "message": "Events Added Successfully",
                    "status": "1"
            })
        else: 
            return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    'nbar': 'events',
                    "message": "Error Unsuccessfully!",
                    "status": "0"
            })

    return render(request, "manager/Events.html", {
        "events": Events.objects.all().order_by('-edate'),
        'nbar': 'events'
    })

def edit_event(request, object_id): 
    object = Events.objects.get(id = object_id)
    if request.method == "POST":
        object.eamount = request.POST["amount"]
        object.edate = request.POST["date"]
        object.titie = request.POST["title"]
        object.edescription = request.POST["description"]
        if object is not None:
            object.save()
            return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    'nbar': 'events',
                    "message": "Event Edited Successfully",
                    "status": "1",
            })
    else:
        return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    'nbar': 'events',
                    'form_data': object,
                    "date": str(object.edate)
            })


def delete_event(request, object_id):
    object = Events.objects.get(id = object_id) 
    object.delete()     

    return render(request, "manager/Events.html", {
        "message": "Events Deleted Successfully",
        'status': '0',
        "events": Events.objects.all().order_by('-edate'),
        'nbar': 'events',
    })

def eventsExpense(request): 
    if request.method == "POST":
        etitle = request.POST["title"]
        eamount = request.POST["amount"]
        edate = request.POST["date"]
        event = request.POST["event"]
        user = request.POST["user"]
        e = EventsExpense(eamount = eamount ,edate = edate, etitle = etitle, event = event, user = user)
        if e is not None: 
            e.save()
            return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    'nbar': 'Events',
                    "message": "Event Expense Added Successfully",
                    "status": "1"
            })
        else: 
            return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    'nbar': 'events',
                    "message": "Error Unsuccessfully!",
                    "status": "0"
            })

    return render(request, "manager/Events.html", {
        "events": Events.objects.all().order_by('-edate'),
        "event_title": Events.event_title.all().filter(event = title).order_by('-edate'),
        'nbar': 'events',
    })

def view_eventsExpense(request, object_id): 
    object = Events.objects.get(id = object_id)
    title = object.etitle
    events_expense_list = EventsExpense.objects.values().filter(event = title).order_by('-edate')

    if events_expense_list is not None:    
        return render(request, "manager/Events.html", {
            "events": Events.objects.all().order_by('-edate'),
            "events_expense_list": events_expense_list,
            'nbar': 'events',
        })

    else:
        return render(request, "manager/Events.html", {
            "events": Events.objects.all().filter(event = title).order_by('-edate'),
            "events_expense_list": events_expense_list,
            'nbar': 'events',
       })

def edit_eventsExpense(request, object_id): 
    object = EventsExpense.objects.get(id = object_id)
    title = object.etitle
    events_expense_list = EventsExpense.objects.values().filter(event = title).order_by('-edate')

    if request.method == "POST":
        object.eamount = request.POST["amount"]
        object.edate = request.POST["date"]
        object.etitle = request.POST["title"]
        object.event = request.POST["event"]
        if object is not None:
            object.save()
            return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    "events_expense_list": events_expense_list,
                    'nbar': 'events',
                    "message": "Event Edited Successfully",
                    "status": "1",
            })
    else:
        return render(request, "manager/Events.html", {
                    "events": Events.objects.all().order_by('-edate'),
                    "events_expense_list": events_expense_list,
                    'nbar': 'events',
                    'form_data_e': object,
                    "edate": str(object.edate)
            })


def delete_eventsExpense(request, object_id):
    object = EventsExpense.objects.get(id = object_id) 
    object.delete()     

    return render(request, "manager/Events.html", {
        "message": "Events Deleted Successfully",
        'status': '0',
        "events": Events.objects.all() .order_by('-edate'),
        'nbar': 'events',
    })

def edit_expense(request, object_id): 
    object = Expense.objects.get(id = object_id)
    if request.method == "POST":
        object.expenseAmount = request.POST["amount"]
        object.expenseDate = request.POST["date"]
        object.expenseCategory = request.POST["category"]
        object.expenseDescription = request.POST["description"]
        if object is not None:
            object.save()
            return render(request, "manager/expense.html", {
                    "expense": Expense.objects.all().order_by('-expenseDate'),
                    'nbar': 'expense',
                    "message": "Expense Edited Successfully",
                    "status": "1",
            })
    else:
        return render(request, "manager/expense.html", {
                    "expense": Expense.objects.all().order_by('-expenseDate'),
                    'nbar': 'expense',
                    'form_data': object,
                    "date": str(object.expenseDate)
            })


def delete_expense(request, object_id):
    object = Expense.objects.get(id = object_id) 
    object.delete()     

    return render(request, "manager/expense.html", {
        "message": "Expense Deleted Successfully",
        'status': '0',
        "expense": Expense.objects.all().order_by('-expenseDate'),
        'nbar': 'expense',
    })

def edit_income(request, object_id): 
    object = Income.objects.get(id = object_id)
    if request.method == "POST":
        object.incomeAmount = request.POST["amount"]
        object.incomeDate = request.POST["date"]
        object.incomeCategory = request.POST["category"]
        object.incomeDescription = request.POST["description"]
        if object is not None:
            object.save()
            return render(request, "manager/income.html", {
                    "income": Income.objects.all().order_by('-incomeDate'),
                    'nbar': 'income',
                    "message": "Income Edited Successfully",
                    "status": "1",
            })
    else:
        return render(request, "manager/income.html", {
                    "income": Income.objects.all().order_by('-incomeDate'),
                    'nbar': 'income',
                    'form_data': object,
                    "date": str(object.incomeDate)
            })


def delete_income(request, object_id):
    object = Income.objects.get(id = object_id) 
    object.delete()     

    return render(request, "manager/income.html", {
        "message": "Income Deleted Successfully",
        'status': '0',
        "income": Income.objects.all().order_by('-incomeDate'),
        'nbar': 'income',
    })

def profile(request): 
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            username = request.POST["username"]
            request.user.get_full_name = name
            request.user.get_username = username
            request.user.email = email
            return render(request, "manager/profile.html", {
                    "message": "User Edited!",
                })

    return render(request, "manager/profile.html", {
        'nbar': 'profile',
    })

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        now = datetime.datetime.now()
        data = {
            "expensePieData": Expense.objects.values('expenseCategory','user').annotate(Sum('expenseAmount')),
            "expenseLineData": Expense.objects.annotate(m=Month('expenseDate')).values('m','user').annotate(Sum('expenseAmount')).order_by(),
            "incomePieData": Income.objects.values('incomeCategory', 'user').annotate(Sum('incomeAmount')),
            "incomeLineData": Income.objects.annotate(m=Month('incomeDate')).values('m','user').annotate(Sum('incomeAmount')).order_by(),
            "property": property.objects.values(),
            "p": property.objects.values('user').annotate(Sum('bamt')),
            "m": gold.objects.values('user').annotate(Sum('bamt')),
            "f": fd.objects.values('user').annotate(Sum('samt')),
            "pp": ppf.objects.values('user').annotate(Sum('samt')),
            "gold": gold.objects.values(),
            "fd": fd.objects.values(),
            "fdd": {
                'date': fd.objects.annotate(m=Month('date')).values('m'),
                'today': now.strftime('%m'),
            },
            "ppf": ppf.objects.values(),
            "ppd": {
                'date': ppf.objects.annotate(m=Month('date')).values('m'),
                'today': now.strftime('%m'),
            },
        }

        return Response(data)

def exportExpense(request):
    expense_resource = ExpenseResource()
    dataset = expense_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Expenses.xls"'
    return response

def exportIncome(request):
    income_resource = IncomeResource()
    dataset = income_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Income.xls"'
    return response
