from django.shortcuts import render
from .models import Journals, JournalsCategory
from .filters import JournalFilter
from .utils import paginateItems, searchItems
import uuid
# Create your views here.

def journals(request):
    # journals = Journals.objects.filter(is_published = True)
    # journal_form = JournalFilter(request.GET, queryset=journals)
    
    # journals = journal_form.qs

    journals, search_query, all_journals = searchItems(request)
    custom_range, journals = paginateItems(request, journals, 2)

    journal_cat = JournalsCategory.objects.all()

    print(journals)

    context = {
        # 'journal_form':journal_form,
        'journals': journals,
        'journal_cat': journal_cat,
        'search_query': search_query,
        'all_journals': all_journals,
        'custom_range': custom_range
    }
    return render(request, 'journals/journals.html', context)