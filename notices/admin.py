from django.contrib import admin
from .models import Notice
from .forms import NoticeRichTextForm

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    form = NoticeRichTextForm

admin.site.register(Notice, NoticeAdmin)