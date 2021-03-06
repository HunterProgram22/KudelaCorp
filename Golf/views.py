from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Round
from .forms import RoundForm, CourseForm
from .functions import calcHandicap, yearAverages


class Home(View):
    def get(self, request):
        year_stats_18 = self.get_year_stats_18()
        year_stats_9 = self.get_year_stats_9()
        context = { 'year_stats_18': year_stats_18,
                    'year_stats_9': year_stats_9
                    }
        return render(request, 'Golf/Home.html', context)

    def get_year_stats_18(self):
        '''Method for totaling all annual stats for 18-hole rounds.'''
        year_stats_18 = []
        years_played_18 = []
        rounds_18 = Round.objects.filter(holesplayed=18).order_by('-date')
        for round_18 in rounds_18:
            if round_18.get_year() not in years_played_18:
                years_played_18.append(round_18.get_year())
        for year_18 in years_played_18:
            year_rounds_18 = Round.objects.filter(date__year=year_18).filter(holesplayed=18)
            year_stats_18.append(yearAverages(year_rounds_18))
        return year_stats_18

    def get_year_stats_9(self):
        '''Method for totaling all annual stats for 9-hole rounds.'''
        year_stats_9 = []
        years_played_9 = []
        rounds_9 = Round.objects.filter(holesplayed=9).order_by('-date')
        for round_9 in rounds_9:
            if round_9.get_year() not in years_played_9:
                years_played_9.append(round_9.get_year())
        for year_9 in years_played_9:
            year_rounds_9 = Round.objects.filter(date__year=year_9).filter(holesplayed=9)
            year_stats_9.append(yearAverages(year_rounds_9))
        return year_stats_9


class Manage(View):
    def get(self, request):
        context = None
        return render(request, 'Golf/Manage.html', context)


class Rounds9(View):
    def get(self, request):
        round_stats_9 = Round.objects.filter(holesplayed=9).order_by('-date')
        context = {'round_stats_9':round_stats_9}
        return render(request, 'Golf/Rounds9.html', context)


class Rounds18(View):
    def get(self, request):
        round_stats_18 = Round.objects.filter(holesplayed=18).order_by('-date')
        context = {'round_stats_18': round_stats_18}
        return render(request, 'Golf/Rounds18.html', context)


class Handicap(View):
    def get(self, request):
        round_handicap_18 = self.get_round_handicap_18()
        round_handicap_18.reverse()
        round_handicap_9 = self.get_round_handicap_9()
        round_handicap_9.reverse()
        context = { 'round_handicap_18': round_handicap_18,
                    'round_handicap_9' : round_handicap_9,
                    }
        return render(request, 'Golf/Handicap.html', context)

    def get_round_handicap_18(self):
        round_stats = Round.objects.filter(holesplayed=18).order_by('date')
        round_handicap = []
        diffList = []
        handicapTotal = 0
        round_count = 0
        for round in round_stats:
            round_count += 1
            diffList.append(round.handicap_diff())
            #There is probably a more efficient way to do this instead of copying the list each time (yield? enumerate?)
            diffUsed = diffList[:]
            if round_count > 20:
                diffUsed = diffUsed[(round_count-20):round_count]
            handicapTotal = calcHandicap((round_count), diffUsed)
            round_handicap.append((round, round.handicap_diff(), handicapTotal))
        return round_handicap

    def get_round_handicap_9(self):
        round_stats9 = Round.objects.filter(holesplayed=9).order_by('date')
        round_handicap9 = []
        diffList9 = []
        handicapTotal9 = 0
        round_count9 = 0
        for round9 in round_stats9:
            round_count9 += 1
            diffList9.append(round9.handicap_diff())
            #There is probably a more efficient way to do this instead of copying the list each time (yield? enumerate?)
            diffUsed9 = diffList9[:]
            if round_count9 > 20:
                diffUsed9 = diffUsed9[(round_count9-20):round_count9]
            handicapTotal9 = calcHandicap((round_count9), diffUsed9)
            round_handicap9.append((round9, round9.handicap_diff(), handicapTotal9))
        return round_handicap9


class NewRound(View):
    def post(self, request):
        form = RoundForm(request.POST)
        if form.is_valid():
            round = form.save()
            # Add user save at later point here
            round.save()
            return redirect('Golf_Manage')
        context = {'form': form}
        return render(request, 'Golf/NewRound.html', context)

    def get(self, request):
        form = RoundForm()
        context = {'form': form}
        return render(request, 'Golf/NewRound.html', context)


class NewCourse(View):
    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            # Add user save at later point here
            course.save()
            return redirect('Golf_Manage')
        context = {'form': form}
        return render(request, 'Golf/NewCourse.html', context)

    def get(self, request):
        form = CourseForm()
        context = {'form': form}
        return render(request, 'Golf/NewCourse.html', context)


class DeleteRound(View):
    def post(self, request):
        print('Test')
        print(request)
        id = int(request.path.replace("/Golf/Golf/DeleteRound/", ""))
        #id = 1
        round = Round.objects.get(pk=id)
        if round.holesplayed == 18:
            round.delete()
            return redirect('Golf_Rounds18')
        elif round.holesplayed == 9:
            round.delete()
            return redirect('Golf_Rounds9')
