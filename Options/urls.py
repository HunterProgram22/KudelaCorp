from django.urls import path
from .views import Home, Manage, Options_new
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Home.as_view()), name='Options_Home'),
    path('Options/Manage', login_required(Manage.as_view()), name='Options_Manage'),
    path('Options/Options_new', login_required(Options_new.as_view()), name='Options_OptionNew'),
    ]
