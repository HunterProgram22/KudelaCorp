from django.urls import path
from .views import Home, Manage, Balance, Balance_new, Income, Income_new, \
    Cash, Analysis, Reports
from django.contrib.auth.decorators import login_required


urlpatterns = [
        path('Finance/Manage', login_required(Manage.as_view()), name='Finance_Manage'),
        path('Finance/Analysis', login_required(Analysis.as_view()), name='Finance_Analysis'),
        path('Finance/Reports', login_required(Reports.as_view()), name='Finance_Reports'),
        path('Finance/Balance', login_required(Balance.as_view()), name='Finance_Balance'),
        path('Finance/Balance_new', login_required(Balance_new.as_view()), name='Finance_Balance_new'),
        path('Finance/Income', login_required(Income.as_view()), name='Finance_Income'),
        path('Finance/Income_new', login_required(Income_new.as_view()), name='Finance_Income_new'),
        path('Finance/Cash', login_required(Cash.as_view()), name='Finance_Cash'),
        path('', login_required(Home.as_view()), name='Finance_Home'),
    ]
