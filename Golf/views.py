from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Round
from .functions import calcHandicap, yearAverages


class Home(View):
    def get(self, request):
        latest_round_list = Round.objects.order_by('-date')[:5]
        year_stats = []
        years_played = []
        rounds = Round.objects.filter(holesplayed=18).order_by('-date')
        #rolling_averages = rollingAverages(rounds)
        for round in rounds:
            if round.get_year() not in years_played:
                years_played.append(round.get_year())
        for year in years_played:
            year_rounds = Round.objects.filter(date__year=year).filter(holesplayed=18)
            year_stats.append(yearAverages(year_rounds))
        context = { 'latest_round_list': latest_round_list,
                    'year_stats': year_stats
                    }
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
