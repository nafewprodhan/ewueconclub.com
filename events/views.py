from django.http import request
from django.shortcuts import redirect, render
from .models import EventCategorie

# Create your views here.

def redirectEvents(request):
    return redirect('events')

def events(request):

    event_cats = EventCategorie.objects.all()
    events_year = event_cats[0].event_set.all()

    context = {'event_cats': event_cats, 'events_year': events_year}

    return render(request, 'events/events.html', context)

def eventCategory(request,pk):
    event_cats = EventCategorie.objects.all()
    event_cat = EventCategorie.objects.get(id=pk)

    events_year = event_cat.event_set.all()

    context = {'event_cats': event_cats, 'events_year': events_year}

    return render(request, 'events/events.html', context)

def event(request,pk):
    return render(request, 'events/single-event.html')