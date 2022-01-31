from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Profile

def paginateItems(request, items, results):

    page = request.GET.get('page')
    paginator = Paginator(items, results)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, items


def searchItems(request):

    search_query = ''
    item = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    if request.GET.get('item'):
        item = request.GET.get('item')

    items = Profile.objects.distinct().filter(
        Q(verified=True) &
        (Q(headline__icontains=search_query) |
        Q(skill__name__icontains=search_query) |
        Q(experience__headline__icontains=search_query)) &
        Q(std_alum__icontains=item)
    )
    
    return items, search_query, item


def paginateBloods(request, items, results):

    page = request.GET.get('page')
    paginator = Paginator(items, results)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, items


def searchBloods(request):

    search_query = ''
    item = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    if request.GET.get('item'):
        item = request.GET.get('item')

    items = Profile.objects.distinct().filter(
        Q(verified=True) &
        (Q(blood_group__icontains=search_query) &
        Q(location__icontains=item))
    )
    
    return items, search_query, item
