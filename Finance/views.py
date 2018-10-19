from django.shortcuts import render, redirect
from django.views import View
from .forms import MonthBalForm, MonthIncForm
from .models import MonthBal, MonthInc
from .functions import report, get_report_criteria, get_analysis_data


class Home(View):
    def get(self, request):
        dash_balance = MonthBal.objects.latest('date')
        dash_income = MonthInc.objects.latest('date')
        return render(request, 'Finance/home.html', {'dash_balance': dash_balance,
        'dash_income': dash_income})

class Manage(View):
    def get(self, request):
        return render(request, 'Finance/manage.html', {})

class Reports(View):
    def get(self, request):
        return render(request, 'Finance/reports.html', {})

    def post(self, request):
        this_quarter, this_year, last_quarter, last_quarteryear, \
            current_quarter_report_name, last_quarter_report_name, \
            yearago_quarter_report_name = get_report_criteria(request)
        current_quarter_report = report(this_quarter, this_year)
        last_quarter_report = report(last_quarter, last_quarteryear)
        yearago = str(int(this_year)-1)
        yearago_quarter_report = report(this_quarter, yearago)
        ''' _reports are returned as a tuple in the format
        (total_creditcards,total_utilities, total_loans, total_savings)'''
        return render(request, 'Finance/reports.html',
                      {'current_quarter_report': current_quarter_report,
                       'last_quarter_report': last_quarter_report,
                       'yearago_quarter_report': yearago_quarter_report,
                       'current_quarter_report_name': current_quarter_report_name,
                       'last_quarter_report_name': last_quarter_report_name,
                       'yearago_quarter_report_name': yearago_quarter_report_name})


class Analysis(View):
    def get(self, request):
        send_data=[(0,0)]
        return render(request, 'Finance/analysis.html', {'send_data': send_data})

    def post(self, request):
        year = request.POST.get("year")
        if year == "":
            return redirect("Finance_Analysis")
        elif year == "ALL":
            monthly_data = MonthInc.objects.all().order_by('date')
        else:
            monthly_data = MonthInc.objects.filter(date__year=year).order_by('date')
        category = request.POST.get("category")
        if category == "":
            return redirect("Finance_Analysis")
        send_data = get_analysis_data(monthly_data, category)
        return render(request, 'Finance/analysis.html',
                    {'send_data': send_data,
                     'category': category,
                     'year': year})

class Balance(View):
    def get(self, request):
        month_balance = MonthBal.objects.order_by('-date')[:2]
        month_balance = month_balance[::-1]
        return render(request, 'Finance/balancesheet.html', {'month_balance': month_balance})

    def post(self, request):
        if request.POST.get("month") != '' and request.POST.get("year") != '':
            month = request.POST.get("month")
            year = request.POST.get("year")
            month_balance = MonthBal.objects.filter(date__month=month).filter(date__year=year)
            month_balance = list(month_balance[:])
            add_month = MonthBal.objects.order_by('-date')[0:1]
            month_balance.append(add_month[0])
        elif request.POST.get("month") != '':
            month = request.POST.get("month")
            month_balance = MonthBal.objects.filter(date__month=month).order_by('date')
        elif request.POST.get("year") != '':
            year = request.POST.get("year")
            month_balance = MonthBal.objects.filter(date__year=year).order_by('date')
        else:
            month_balance = MonthBal.objects.order_by('-date')[:2]
            month_balance = month_balance[::-1]
        return render(request, 'Finance/balancesheet.html', {'month_balance': month_balance})

class Balance_new(View):
    def post(self, request):
        form = MonthBalForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.save()
            return redirect('Finance_Manage')
        return render(request, 'Finance/balance_edit.html', {'form': form})

    def get(self, request):
        form = MonthBalForm()
        return render(request, 'Finance/balance_edit.html', {'form': form})

class Income(View):
    def get(self, request):
        month_income = MonthInc.objects.order_by('-date')[:2]
        month_income = month_income[::-1]
        return render(request, 'Finance/incomestatement.html', {'month_income': month_income})

    def post(self, request):
        if request.POST.get("month") != '' and request.POST.get("year") != '':
            month = request.POST.get("month")
            year = request.POST.get("year")
            month_income = MonthInc.objects.filter(date__month=month).filter(date__year=year)
            month_income = list(month_income[:])
            add_month = MonthInc.objects.order_by('-date')[0:1]
            month_income.append(add_month[0])
        elif request.POST.get("month") != '':
            month = request.POST.get("month")
            month_income = MonthInc.objects.filter(date__month=month).order_by('date')
        elif request.POST.get("year") != '':
            year = request.POST.get("year")
            month_income = MonthInc.objects.filter(date__year=year).order_by('date')
        else:
            month_income = MonthInc.objects.order_by('-date')[:2]
            month_income = month_income[::-1]
        return render(request, 'Finance/incomestatement.html', {'month_income': month_income})

class Income_new(View):
    def post(self, request):
        form = MonthIncForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Finance_Manage')
        return render(request, 'Finance/income_edit.html', {'form': form})

    def get(self, request):
        form = MonthIncForm()
        return render(request, 'Finance/income_edit.html', {'form': form})

class Cash(View):
    def get(self, request):
        month_cash = MonthInc.objects.all().order_by('-date')[:2]
        month_cash = month_cash[::-1]
        return render(request, 'Finance/cashflow.html', {'month_cash': month_cash})

    def post(self, request):
        if request.POST.get("month") != '' and request.POST.get("year") != '':
            month = request.POST.get("month")
            year = request.POST.get("year")
            month_cash = MonthInc.objects.filter(date__month=month).filter(date__year=year)
            month_cash = list(month_cash[:])
            add_month = MonthInc.objects.order_by('-date')[0:1]
            month_cash.append(add_month[0])
        elif request.POST.get("month") != '':
            month = request.POST.get("month")
            month_cash = MonthInc.objects.filter(date__month=month).order_by('date')
        elif request.POST.get("year") != '':
            year = request.POST.get("year")
            month_cash = MonthInc.objects.filter(date__year=year).order_by('date')
        else:
            month_cash = MonthInc.objects.order_by('-date')[:2]
            month_cash = month_cash[::-1]
        return render(request, 'Finance/cashflow.html', {'month_cash': month_cash})
