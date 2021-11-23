from django.contrib import admin
from .models import EventCategorie, Event, EventTag, EventReview

# Register your models here.
admin.site.register(EventCategorie)
admin.site.register(Event)
admin.site.register(EventTag)
admin.site.register(EventReview)