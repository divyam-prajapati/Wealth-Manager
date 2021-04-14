from django.db import models

# Create your models here.
class Expense(models.Model):
    expenseAmount = models.IntegerField()
    expenseDate = models.DateField()
    expenseCategory = models.CharField(max_length=64)
    expenseDescription = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}  {self.expenseAmount}   {self.expenseDate}   {self.expenseCategory}  {self.expenseDescription}"

class Income(models.Model):
    incomeAmount = models.IntegerField()
    incomeDate = models.DateField()
    incomeCategory = models.CharField(max_length=64)
    incomeDescription = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}  {self.incomeAmount}   {self.incomeDate}   {self.incomeCategory}  {self.incomeDescription}"

