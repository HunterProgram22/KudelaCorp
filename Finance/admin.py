from django.contrib import admin
from .models import MonthBal, MonthInc, TaxReturn

admin.site.register(MonthBal)
admin.site.register(MonthInc)
admin.site.register(TaxReturn)
