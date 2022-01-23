# from django.db.models.signals import post_save, post_delete

# from django.contrib.auth.models import User
# from .models import Event
# from user.models import Profile

# from django.conf import settings


# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template


# def sendEventMail(sender, instance, created, **kwargs):
#     if created:
#         event = instance

#         allemail = Profile.objects.all()

#         for mail in allemail:
#             context = {'event': event, 'profile': allemail}
#             html_template = get_template("events/event-email-template.html").render(context)
#             email = EmailMultiAlternatives(subject="test - send event mail template", from_email="ewueconclubnet@gmail.com", to=[mail.email])
#             email.attach_alternative(html_template, 'text/html')
#             email.send()
#             print(mail)
            

# post_save.connect(sendEventMail, sender=Event)