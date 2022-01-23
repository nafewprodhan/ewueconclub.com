from django.contrib import admin
from .models import Eblog, EblogCategorie, EblogTag, EblogReview
from .forms import EblogAdminForm

class EblogAdmin(admin.ModelAdmin):
    form = EblogAdminForm

admin.site.register(Eblog, EblogAdmin)
admin.site.register(EblogCategorie)
admin.site.register(EblogTag)
admin.site.register(EblogReview)