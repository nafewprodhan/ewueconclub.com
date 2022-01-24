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

    notice_alum = []
    notice_gm = []

    for notice in notices:
        if str(notice.notice_to) == "GM":
            notice_alum.append(notice)
        elif str(notice.notice_to) == "AL":
            notice_gm.append(notice)

    print(notice_alum)
    print(notice_gm)

    # for profile in profile_al:
    #     print(profile.email)

    context = {'notices': notices, 'notice_alum': notice_alum, 'notice_gm': notice_gm}
        
    return render(request, 'notices/notices.html', context)


def notice(request, pk):
    notice = Notice.objects.get(id=pk)

    context = {'notice': notice}

    return render(request, 'notices/single-notice.html', context)