from django.contrib import admin
from .models import Epub, EpubAuthor, EpubCategory
# Register your models here.

admin.site.register(Epub)
admin.site.register(EpubAuthor)
admin.site.register(EpubCategory)