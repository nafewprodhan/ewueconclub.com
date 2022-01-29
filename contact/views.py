from django.conf import settings
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            if request.user.is_authenticated:
                contact_form = form.save(commit=False)
                contact_form.name = request.user.profile.name
                contact_form.email = request.user.email
                from_email = contact_form.email
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                contact_form.save()
            else:
                name = form.cleaned_data['name']
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                form.save()
                
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            messages.success(request, 'Success! Thank you for your message.')
            return redirect('contact')
    return render(request, "contact/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')