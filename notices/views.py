from django.shortcuts import render
from .models import Notice
from user.models import Profile

# Create your views here.

def notices(request):

    profile_all = Profile.objects.all()
    profile_gm = Profile.objects.filter(std_alum = "student")
    profile_al = Profile.objects.filter(std_alum = "alumnus")
    profile_fc = Profile.objects.filter(faculty = True)

    notices = Notice.objects.all()

    for notice in notices:
        # print(notice.notice_to)
        if str(notice.notice_to) == "AL":
            print("Notice- alum " + notice.title)

    for profile in profile_al:
        print(profile.email)
        

    return render(request, 'notices/notices.html')