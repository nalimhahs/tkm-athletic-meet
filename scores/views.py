from django.shortcuts import render

from .models import *

# Create your views here.


def main_view(request):

    events = Event.objects.all()

    first_year_score = Event.objects.filter(first__year=1).count()*5 + Event.objects.filter(second__year=1).count()*3 + Event.objects.filter(third__year=1).count()*1
    second_year_score = Event.objects.filter(first__year=2).count()*5 + Event.objects.filter(second__year=2).count()*3 + Event.objects.filter(third__year=2).count()*1
    third_year_score = Event.objects.filter(first__year=3).count()*5 + Event.objects.filter(second__year=3).count()*3 + Event.objects.filter(third__year=3).count()*1
    fourth_year_score = Event.objects.filter(first__year=4).count()*5 + Event.objects.filter(second__year=4).count()*3 + Event.objects.filter(third__year=4).count()*1

    return render(request, 'index.html', { 'events': events, 'first_year_score': first_year_score, 'second_year_score': second_year_score, 'third_year_score': third_year_score, 'fourth_year_score': fourth_year_score })