from django.shortcuts import render
from django.http import HttpResponse

from .models import Round

def index(request):
    latest_round_list = Round.objects.order_by('-date')[:5]
    context = {'latest_round_list': latest_round_list}
    return render(request, 'Golf/index.html', context)

def detail(request, round_id):
    return HttpResponse("You're looking at round %s." % round_id)

def results(request, round_id):
    return HttpResponse("You're lookin at the results of round %s." % round_id)
