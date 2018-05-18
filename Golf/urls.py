from django.urls import path
from .views import Home, Manage, Rounds9, Rounds18, Handicap, NewRound, NewCourse
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Home.as_view()), name='Golf_Home'),
    path('Golf/Manage/', login_required(Manage.as_view()), name='Golf_Manage'),
    path('Golf/Rounds9/', login_required(Rounds9.as_view()), name='Golf_Rounds9'),
    path('Golf/Rounds18/', login_required(Rounds18.as_view()), name='Golf_Rounds18'),
    path('Golf/Handicap/', login_required(Handicap.as_view()), name='Golf_Handicap'),
    path('Golf/NewRound/', login_required(NewRound.as_view()), name='Golf_NewRound'),
    path('Golf/NewCourse/', login_required(NewCourse.as_view()), name='Golf_NewCourse'),
]
