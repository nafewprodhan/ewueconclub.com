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

    # eblog_tags = EblogTag.objects.filter(name__icontains=search_query)
    
    # =====================
    
    # p = Profile.objects.all()
    # sk=None

    # for i in p:
    #     sk = i.skill_set.get(name__icontains=search_query)
    #     print(sk)

    # =====================

    # if search_query == '' and item == '':
    #     items = Profile.objects.filter(verified=True)
    # elif search_query and item == '':
    #     items = Profile.objects.distinct().filter(
    #         Q(verified=True) &
    #         (Q(title__icontains=search_query) |
    #         Q(body__icontains=search_query) |
    #         Q(eblog_tags__in=eblog_tags))
    #     )
    # else:

    items = Profile.objects.distinct().filter(
        Q(verified=True) &
        (Q(headline__icontains=search_query) |
        Q(skill__name__icontains=search_query)) &
        Q(std_alum__icontains=item)
    )
    
    return items, search_query, item
