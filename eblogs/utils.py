from .models import Eblog, EblogTag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = EblogTag.objects.filter(name__icontains=search_query)

    items = Eblog.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(body__icontains=search_query) |
        Q(eblog_tags__in=tags)
    )
    return items, search_query
