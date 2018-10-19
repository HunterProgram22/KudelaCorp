from .models import MonthInc, MonthBal


def report(quarter, year):
    qmonthstart, qmonthend, qmonthbal, qyearbal = get_quarter_months(quarter, year)
    quartermonths = MonthInc.objects.filter(date__year=year).filter(
        date__month__gte=qmonthstart, date__month__lte=qmonthend)
    creditcards, utilities, loans, savings, surplus = get_quarter_income(quartermonths)
    networth, loanbalance, savingsbalance = get_quarter_balance(qmonthbal, qyearbal)
    return (creditcards, utilities, loans, savings, surplus, networth, loanbalance, savingsbalance)


def get_report_criteria(request):
    quarter = request.POST.get("quarter")[0]
    year = request.POST.get("quarter")[2:]
    quarter_report_name = quarter + "Q " + year
    yearago_report_name = quarter + "Q " + str(int(year)-1)
    if quarter == "1":
        lastquarter_month = "4"
        lastquarter_year = str(int(year)-1)
    else:
        lastquarter_month = str(int(quarter)-1)
        lastquarter_year = year
    last_quarter_report_name = lastquarter_month + "Q " + lastquarter_year
    return (quarter, year, lastquarter_month, lastquarter_year, \
        quarter_report_name, last_quarter_report_name, yearago_report_name)

def get_quarter_months(quarter, year):
    '''monthbal is set to month after end of quarter
    to get the true balances at the end of quarter b/c
    statements are as of 1st of a month'''
    yearbal = year
    if quarter == "1":
        monthstart, monthend, monthbal = "1", "3", "4"
    elif quarter == "2":
        monthstart, monthend, monthbal = "4", "6", "7"
    elif quarter == "3":
        monthstart, monthend, monthbal = "7", "9", "10"
    elif quarter == "4":
        monthstart, monthend, monthbal = "10", "12", "1"
        yearbal = str(int(year)+1)
    return (monthstart, monthend, monthbal, yearbal)


def get_quarter_income(quartermonths):
    creditcards, utilities, loans, savings, surplus = 0, 0, 0, 0, 0
    for months in quartermonths:
        creditcards += months.total_personal_creditcards()
        utilities += months.total_utilities()
        loans += months.total_loans()
        savings += months.total_allsavings()
        surplus += months.total_surplus()
    return (creditcards, utilities, loans, savings, surplus)


def get_quarter_balance(qmonthbal, qyearbal):
    quarter_end = MonthBal.objects.filter(date__year=qyearbal).filter(
        date__month=qmonthbal)
    try:
        networth = quarter_end[0].networth()
        loanbalance = quarter_end[0].total_loan()
        savingsbalance = quarter_end[0].total_save()
    except IndexError:
        networth, loanbalance, savingsbalance = 'N/A', 'N/A', 'N/A'
    return (networth, loanbalance, savingsbalance)


def get_analysis_data(monthly_data, category):
    send_data = []
    for item in monthly_data:
        month = item.date
        amount = getattr(item, category)
        send_data.append((month, amount))
    return send_data
