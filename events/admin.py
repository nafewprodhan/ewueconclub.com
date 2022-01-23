from django import forms
from django.contrib import admin
from .models import EventCategorie, Event, EventTag, EventReview
from .forms import EventRichTextForm
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    form = EventRichTextForm

admin.site.register(Event, EventAdmin)
admin.site.register(EventCategorie)
admin.site.register(EventTag)
admin.site.register(EventReview)