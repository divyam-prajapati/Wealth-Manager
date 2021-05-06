from django.db import models
from django.db.models import Func,F
# Create your models here.

class Month (Func):
    function = 'STRFTIME'
    template = '%(function)s("%%m", %(expressions)s)'
    output_field = models.IntegerField()

class Expense(models.Model):
    user = models.CharField(max_length = 64)
    expenseAmount = models.IntegerField()
    expenseDate = models.DateField()
    expenseCategory = models.CharField(max_length=64)
    expenseDescription = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}  {self.expenseAmount}   {self.expenseDate}   {self.expenseCategory}  {self.expenseDescription}"

class Income(models.Model):
    user = models.CharField(max_length = 64)
    incomeAmount = models.IntegerField()
    incomeDate = models.DateField()
    incomeCategory = models.CharField(max_length=64)
    incomeDescription = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}  {self.incomeAmount}   {self.incomeDate}   {self.incomeCategory}  {self.incomeDescription}"


class property(models.Model): 
    user = models.CharField(max_length = 64)
    sqft = models.IntegerField()
    date = models.DateField()
    bamt = models.IntegerField()
    des = models.CharField(max_length=64)
    cpsqft = models.IntegerField(null = True)

class gold(models.Model): 
    user = models.CharField(max_length = 64)
    gms = models.FloatField()
    date = models.DateField()
    bamt = models.IntegerField()
    type = models.CharField(max_length=64)
    des = models.CharField(max_length=64)
    cpm = models.IntegerField(null = True)

class fd(models.Model): 
    user = models.CharField(max_length = 64)
    samt = models.IntegerField()
    date = models.DateField()
    int = models.FloatField()
    des = models.CharField(max_length=64)

class ppf(models.Model): 
    user = models.CharField(max_length = 64)
    samt = models.IntegerField()
    date = models.DateField()
    int = models.FloatField()
    des = models.CharField(max_length=64)

class Events(models.Model):
    user = models.CharField(max_length = 64)
    eamount = models.IntegerField()
    edate = models.DateField()
    etitle = models.CharField(max_length=64)
    edescription = models.CharField(max_length=64)

class EventsExpense(models.Model):
    user = models.CharField(max_length = 64)
    eamount = models.IntegerField()
    edate = models.DateField()
    etitle = models.CharField(max_length=64)
    event = models.CharField(max_length=64)