from django.contrib import admin

from .models import Profile, Skill, Education, Experience, Executivecommittiee, Moderator

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'verified','blood_group', 'institution', 'department')
    list_display_links = ('username',)
    list_filter = ('verified', 'institution', 'blood_group', 'faculty', 'std_alum')
    list_editable = ('verified',)
    search_fields = ('username', 'name', 'email', 'blood_group', 'institution', 'department', 'location')
    list_per_page = 25

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)

admin.site.register(Executivecommittiee)
admin.site.register(Moderator)