from django.contrib import admin
from .models import JournalKeyword, Journals, JournalsCategory, JournalAuthor

# Register your models here.

admin.site.register(Journals)
admin.site.register(JournalsCategory)
admin.site.register(JournalAuthor)
admin.site.register(JournalKeyword)