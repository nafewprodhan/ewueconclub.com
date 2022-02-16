from django.shortcuts import render, redirect
from .models import JournalsCategory, Journals
from .forms import JournalReviewForm
from django.contrib import messages
from .utils import paginateItems, searchItems
# Create your views here.

def journals(request):
    journals, search_query, all_journals = searchItems(request)
    custom_range, journals = paginateItems(request, journals, 4)

    journal_cat = JournalsCategory.objects.all()

    print(journals)

    context = {
        'journals': journals,
        'journal_cat': journal_cat,
        'search_query': search_query,
        'all_journals': all_journals,
        'custom_range': custom_range
    }
    return render(request, 'journals/journals.html', context)

def journal(request, pk):
    journal = Journals.objects.get(id=pk)
    journal_cat = journal.all_journals
    form = JournalReviewForm()
    related_journals = Journals.objects.filter(all_journals=journal_cat)

    if request.method == 'POST':
        form = JournalReviewForm(request.POST)
        review = form.save(commit=False)
        review.journal = journal
        review.owner = request.user.profile
        review.save()  

        messages.success(request, 'Your comment was successfully submitted!')
        return redirect('journal', pk=journal.id)

    context = {'journal': journal, 'form': form, 'journal_cat': journal_cat, 'rjournals': related_journals}
    return render(request, 'journals/single-journal.html', context)