from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Eblog, EblogTag

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
    all_blogs = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    if request.GET.get('all_blogs'):
        all_blogs = request.GET.get('all_blogs')

    eblog_tags = EblogTag.objects.filter(name__icontains=search_query)
    
    # ==================
    
    # =====================

    if search_query == '' and all_blogs == '':
        items = Eblog.objects.filter(is_published=True)
    elif search_query and all_blogs == '':
        items = Eblog.objects.distinct().filter(
            Q(is_published=True) &
            (Q(title__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(eblog_tags__in=eblog_tags))
        )
    else:
        items = Eblog.objects.distinct().filter(
            Q(is_published=True) &
            (Q(title__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(eblog_tags__in=eblog_tags)) &
            Q(eblog_cats__title=all_blogs)
        )
    
    return items, search_query, all_blogs
