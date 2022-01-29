from django.shortcuts import render

# Create your views here.

def journals(request):
    return render(request, 'journals/journals.html')