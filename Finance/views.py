from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from .forms import MonthBalForm, MonthIncForm, TaxReturnForm
from .models import MonthBal, MonthInc, TaxReturn
from .functions import report, get_report_criteria, get_analysis_data


class Home(View):
    def get(self, request):
        dash_balance = MonthBal.objects.latest('date')
        dash_income = MonthInc.objects.latest('date')
        return render(request, 'Finance/Home.html', {'dash_balance': dash_balance,
        'dash_income': dash_income})


class Manage(View):
    def get(self, request):
        return render(request, 'Finance/Manage.html', {})


class Reports(View):
    def get(self, request):
        return render(request, 'Finance/Reports.html', {})

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
        return render(request, 'Finance/Reports.html',
                      {'current_quarter_report': current_quarter_report,
                       'last_quarter_report': last_quarter_report,
                       'yearago_quarter_report': yearago_quarter_report,
                       'current_quarter_report_name': current_quarter_report_name,
                       'last_quarter_report_name': last_quarter_report_name,
                       'yearago_quarter_report_name': yearago_quarter_report_name})


class Analysis(View):
    def get(self, request):
        print(request)
        send_data=[(0,0)]
        context = {'send_data': send_data}
        return render(request, 'Finance/Analysis.html', context)

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
        context = { 'send_data': send_data,
                    'category': category,
                    'year': year}
        return render(request, 'Finance/Analysis.html', context)


class Balance(View):
    def get(self, request):
        month_balance = MonthBal.objects.order_by('-date')[:2]
        month_balance = month_balance[::-1]
        return render(request, 'Finance/Balancesheet.html', {'month_balance': month_balance})

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
            month_balance = MonthBal.objects.filter(date__month=month).order_by('-date')
        elif request.POST.get("year") != '':
            year = request.POST.get("year")
            month_balance = MonthBal.objects.filter(date__year=year).order_by('date')
        else:
            month_balance = MonthBal.objects.order_by('-date')[:2]
            month_balance = month_balance[::-1]
        return render(request, 'Finance/Balancesheet.html', {'month_balance': month_balance})

class Balance_new(View):
    def post(self, request):
        form = MonthBalForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.save()
            return redirect('Finance_Manage')
        return render(request, 'Finance/BalanceEdit.html', {'form': form})

    def get(self, request):
        form = MonthBalForm()
        return render(request, 'Finance/BalanceEdit.html', {'form': form})


class Annual_income(View):
    '''https://stackoverflow.com/questions/2997433/django-filtering-datetime-field-by-only-the-year-value'''
    '''https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query'''
    def get(self, request):
        years = MonthInc.objects.all().dates('date', 'year')
        years = years[::-1]
        fields = MonthInc._meta.get_fields()[2:]
        clean_field_list = []

        for field in fields:
            clean_field_list.append(str(field).split('.')[2])

        multi_year_data = {}

        for year in years:
            year_data = []
            for field in clean_field_list:
                year_income = MonthInc.objects.filter(date__year=year.year)
                year_data.append(year_income.aggregate(Sum(field)))
            multi_year_data[year] = year_data

        template_dict = {}
        for year, datum in multi_year_data.items():
            year_data_dict = {}
            for item in datum:
                for account, value in item.items():
                    year_data_dict[account] = value
            template_dict[year] = year_data_dict

        print(template_dict)
        return render(request, 'Finance/AnnualIncome.html', {'template_dict': template_dict})



class Income(View):
    def get(self, request):
        month_income = MonthInc.objects.order_by('-date')[:2]
        month_income = month_income[::-1]
        return render(request, 'Finance/Incomestatement.html', {'month_income': month_income})

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
        return render(request, 'Finance/Incomestatement.html', {'month_income': month_income})


class Income_new(View):
    def post(self, request):
        form = MonthIncForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Finance_Manage')
        return render(request, 'Finance/IncomeEdit.html', {'form': form})

    def get(self, request):
        form = MonthIncForm()
        return render(request, 'Finance/IncomeEdit.html', {'form': form})

class Cash(View):
    def get(self, request):
        month_cash = MonthInc.objects.all().order_by('-date')[:2]
        month_cash = month_cash[::-1]
        return render(request, 'Finance/Cashflow.html', {'month_cash': month_cash})

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
        return render(request, 'Finance/Cashflow.html', {'month_cash': month_cash})


class Tax_new(View):
    def post(self, request):
        form = TaxReturnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Finance_Manage')
        return render(request, 'Finance/TaxEdit.html', {'form': form})

    def get(self, request):
        form = TaxReturnForm()
        return render(request, 'Finance/TaxEdit.html', {'form': form})


class Taxes(View):
    def get(self, request):
        tax_returns = TaxReturn.objects.order_by('-year')
        tax_returns = tax_returns[::-1]
        context = {'tax_returns': tax_returns}
        return render(request, 'Finance/Taxreturns.html', context)


class Metrics(View):
    def get(self, request):
        context = {}
        return render(request, 'Finance/Metrics.html', context)
