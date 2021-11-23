from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Event, EventCategorie

from .utils import paginateEvents, searchEvents
from .forms import ReviewForm

# Create your views here.

def redirectEvents(request):
    return redirect('events')

def events(request):

    events, search_query = searchEvents(request)
    custom_range, events = paginateEvents(request, events, 4)

    event_cats = EventCategorie.objects.all()

    context = {'event_cats': event_cats, 'search_query': search_query, 'custom_range': custom_range, 'events_year': events}

    return render(request, 'events/events.html', context)

def eventCategory(request,pk):

    event_cats = EventCategorie.objects.all()
    event_cat = EventCategorie.objects.get(id=pk)

    events_year = event_cat.event_set.all()

    custom_range, events = paginateEvents(request, events_year, 4)

    context = {'event_cats': event_cats, 'custom_range': custom_range, 'events_year': events}

    return render(request, 'events/events.html', context)


def event(request,pk):

    eventObj = Event.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.event = eventObj
        review.owner = request.user.profile
        review.save()

        messages.success(request, 'Your comment was successfully submitted!')
        return redirect('event', pk=eventObj.id)

    return render(request, 'events/single-event.html', {'event': eventObj, 'form': form})