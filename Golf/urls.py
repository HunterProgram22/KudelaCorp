from django.urls import path
from .views import Home, Manage, Rounds9, Rounds18

urlpatterns = [
    path('', Home.as_view(), name='Golf_Home'),
    path('Golf/Manage/', Manage.as_view(), name='Golf_Manage'),
    path('Golf/Rounds9/', Rounds9.as_view(), name='Golf_Rounds9'),
    path('Golf/Rounds18/', Rounds18.as_view(), name='Golf_Rounds18'),

]
