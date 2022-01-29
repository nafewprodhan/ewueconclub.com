from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Journals, JournalKeyword

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
    all_journals = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    if request.GET.get('all_journals'):
        all_journals = request.GET.get('all_journals')

    keyword = JournalKeyword.objects.filter(keyword__icontains=search_query)
    
    # ==================
    
    # =====================

    if search_query == '' and all_journals == '':
        items = Journals.objects.filter(is_published=True)
    elif search_query and all_journals == '':
        items = Journals.objects.distinct().filter(
            Q(is_published=True) &
            (Q(title__icontains=search_query) |
            Q(abstract__icontains=search_query) |
            Q(keyword__in=keyword))
        )
    else:
        items = Journals.objects.distinct().filter(
            Q(is_published=True) &
            (Q(title__icontains=search_query) |
            Q(abstract__icontains=search_query) |
            Q(keyword__in=keyword)) &
            Q(all_journals__category=all_journals)
        )
    
    return items, search_query, all_journals
