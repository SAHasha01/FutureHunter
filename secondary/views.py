from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    department = None
    subject = request.GET.get('subject')
    hour = request.GET.get('hour')
    gpa = request.GET.get('gpa')
    virtue = request.GET.get('virtue')
    interested = request.GET.get('interested')
    print(subject, hour, gpa, virtue, interested)

    if subject == 'Math&physics' and (
            hour == '5' or hour == '8') and gpa == '4' and (
            virtue == 'patience' or virtue == 'inventor' or virtue == 'coolmindset' or virtue == 'thinklogically' or virtue == 'imagination') and (
            interested == 'invention' or interested == 'innovative' or interested == 'learnscience'):

        department = "science"

    elif subject == 'history' and (
            hour == '3' or hour == '5') and (gpa == '3' or gpa == '4') and (
            virtue == 'patience' or virtue == 'enthusiastic' or virtue == 'imagination') and (
            interested == 'literature'):
        department = "Arts"
    elif subject == 'math' and (
            hour == '5' or hour == '8') and (gpa == '4' or gpa == '5') and (
            virtue == 'initiative') and (
            interested == 'entrepreneur'):
        department = "Commerce"

    param = {'department': department}

    return render(request, 'index.html', param)
