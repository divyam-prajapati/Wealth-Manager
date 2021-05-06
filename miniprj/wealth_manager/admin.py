from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Expense, Income, property, gold, fd, ppf, Events, EventsExpense

class ExpenseAdmin(ImportExportModelAdmin):
    pass

class IncomeAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income)
admin.site.register(property)
admin.site.register(gold)
admin.site.register(fd)
admin.site.register(ppf)
admin.site.register(Events)
admin.site.register(EventsExpense)

