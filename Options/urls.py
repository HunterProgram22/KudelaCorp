from django.urls import path
from .views import Home
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Home.as_view()), name='Options_Home'),
    ]
