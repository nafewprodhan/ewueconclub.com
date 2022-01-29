import imp
from os import name
from pyexpat import model
from django.forms import fields
import django_filters
from .models import Journals

class JournalFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Journals
        fields = ['title', 'all_journals',]

        labels = {
            'title': 'Title',
            'all_journals': "All Journals"
        }