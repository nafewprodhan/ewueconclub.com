from django.contrib import admin
from .models import EventCategorie, Event

# Register your models here.
admin.site.register(EventCategorie)
admin.site.register(Event)