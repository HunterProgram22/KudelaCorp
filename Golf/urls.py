from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Golf/test/', views.test, name='test'),
]
