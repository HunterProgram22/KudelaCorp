from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Round

@login_required
def index(request):
    latest_round_list = Round.objects.order_by('-date')[:5]
    context = {'latest_round_list': latest_round_list}
    return render(request, 'Golf/GolfBase.html', context)

def test(request):
    latest_round_list = Round.objects.order_by('-date')[:5]
    context = {'latest_round_list': latest_round_list}
    return render(request, 'Golf/test.html', context)
