from .models import Event, EventTag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateEvents(request, events, results):

    page = request.GET.get('page')
    paginator = Paginator(events, results)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        events = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        events = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, events


def searchEvents(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = EventTag.objects.filter(name__icontains=search_query)

    events = Event.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(body__icontains=search_query) |
        Q(place__icontains=search_query) |
        Q(tags__in=tags)
    )
    return events, search_query
