from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import OptionPositionForm
from .models import OptionPosition


class Home(View):
    def get(self, request):
        context = {}
        return render(request, 'Options/Home.html', context)


class Manage(View):
    def get(self, request):
        return render(request, 'Options/Manage.html', {})


class Options_new(View):
    def post(self, request):
        form = OptionPositionForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.save()
            return redirect('Options_Manage')
        return render(request, 'Options/Manage.html', {'form': form})

    def get(self, request):
        form = OptionPositionForm
        return render(request, 'Options/OptionsNew.html', {'form':form})


class Options_open(View):
    def get(self, request):
        open_options = OptionPosition.objects.filter(position_status='Open')
        return render(request, 'Options/OptionsOpen.html', {'open_options':open_options})


class Options_closed(View):
    def get(self, request):
        return render(request, 'Options/OptionsClosed.html', {})
