from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Round


class Home(View):
    def get(self, request):
        latest_round_list = Round.objects.order_by('-date')[:5]
        context = {'latest_round_list': latest_round_list}
        return render(request, 'Golf/GolfBase.html', context)


class Manage(View):
    def get(self, request):
        return render(request, 'Golf/Manage.html', context)


class Rounds9(View):
    def get(self, request):
        #round_stats9 = Round.objects.filter(holesplayed=9).order_by('-date')
        #context = {'round_stats9': round_stats9}
        return render(request, 'Golf/Rounds9.html', context)


class Rounds18(View):
    def get(self, request):
        #round_stats = Round.objects.filter(holesplayed=18).order_by('-date')
        #context = {'round_stats': round_stats}
        return render(request, 'Golf/Rounds.html', context)
