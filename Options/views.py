from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Home(View):
    def get(self, request):
        context = {}
        return render(request, 'Options/Home.html', context)


class Manage(View):
    def get(self, request):
        return render(request, 'Options/Manage.html', {})

class Options_new(View):
    def get(self, request):
        return render(request, 'Options/OptionNew.html', {})
