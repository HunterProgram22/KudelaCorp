from django.urls import path
from .views import Home, Manage, Options_new, Options_open, Options_closed 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Home.as_view()), name='Options_Home'),
    path('Options/Manage', login_required(Manage.as_view()), name='Options_Manage'),
    path('Options/Options_new', login_required(Options_new.as_view()), name='Options_OptionsNew'),
    path('Options/Options_open', login_required(Options_open.as_view()), name='Options_OptionsOpen'),
    path('Options/Options_closed', login_required(Options_closed.as_view()), name='Options_OptionsClosed'),
    ]
