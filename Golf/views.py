from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Round


class Home(View):
    def get(self, request):
        latest_round_list = Round.objects.order_by('-date')[:5]
        context = {'latest_round_list': latest_round_list}
        return render(request, 'Golf/Home.html', context)


class Manage(View):
    def get(self, request):
        context = None
        return render(request, 'Golf/Manage.html', context)


class Rounds9(View):
    def get(self, request):
        #round_stats9 = Round.objects.filter(holesplayed=9).order_by('-date')
        context = None
        return render(request, 'Golf/Rounds9.html', context)


class Rounds18(View):
    def get(self, request):
        #round_stats = Round.objects.filter(holesplayed=18).order_by('-date')
        context = None
        return render(request, 'Golf/Rounds18.html', context)


class Handicap(View):
    def get(self, request):
        context = None
        return render(request, 'Golf/Handicap.html', context)


class NewRound(View):
    def post(self, request):
        # form = RoundForm(request.POST)
        # if form.is_valid():
        #     round = form.save()
        #     # Add user save at later point here
        #     round.save()
        #     return redirect('Golf_Manage')
        context = None # {'form': form}
        return render(request, 'Golf/NewRound.html', context)

    def get(self, request):
        # form = RoundForm()
        context = None #{'form': form}
        return render(request, 'Golf/NewRound.html', context)


class NewCourse(View):
    def post(self, request):
        # form = CourseForm(request.POST)
        # if form.is_valid():
        #     course = form.save()
        #     # Add user save at later point here
        #     course.save()
        #     return redirect('Golf_Manage')
        context = None # {'form': form}
        return render(request, 'Golf/NewCourse.html', context)

    def get(self, request):
        # form = CourseForm()
        context = None #{'form': form}
        return render(request, 'Golf/NewCourse.html', context)
