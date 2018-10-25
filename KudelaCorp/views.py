from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "KudelaCorp/Home.html")

def photos(request):
    return render(request, "KudelaCorp/Index.html")
