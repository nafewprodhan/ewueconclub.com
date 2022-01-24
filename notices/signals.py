# from django.db.models.signals import post_save, post_delete

# from .models import Notice
# from user.models import Profile

# from django.conf import settings

# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template


# def sendNoticeMail(sender, instance, created, **kwargs):
#     if created:
#         notice = instance

#         collect_mail = None

#         if str(notice.notice_to) == "GM":
#             collect_mail = Profile.objects.filter(std_alum = "student")
#         elif str(notice.notice_to) == "AL":
#             collect_mail = Profile.objects.filter(std_alum = "alumnus")
#         elif str(notice.notice_to) == "FC":
#             collect_mail = Profile.objects.filter(faculty = True)
#         else:
#             collect_mail = Profile.objects.all()


#         for mail in collect_mail:
#             context = {'notice': notice, 'mail': collect_mail}
#             html_template = get_template("notices/notices-email-template.html").render(context)
#             email = EmailMultiAlternatives(subject=notice.title, from_email="ewueconclubnet@gmail.com", to=[mail.email])
#             email.attach_alternative(html_template, 'text/html')
#             email.send()
#             print(mail)
            

# post_save.connect(sendNoticeMail, sender=Notice)