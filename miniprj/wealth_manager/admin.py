from django.contrib import admin
from .models import Expense, Income, property, gold, fd, ppf, Events, EventsExpense
# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(property)
admin.site.register(gold)
admin.site.register(fd)
admin.site.register(ppf)
admin.site.register(Events)
admin.site.register(EventsExpense)
