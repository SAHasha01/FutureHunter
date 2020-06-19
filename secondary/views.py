from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    subject = request.GET.get('subject')
    hour = request.GET.get('hour')
    gpa = request.GET.get('gpa')
    virtue = request.GET.get('virtue')
    interested = request.GET.get('interested')
    print(subject,hour,gpa,virtue,interested)





    param = {'question': subject}


    return render(request, 'index.html', param)
