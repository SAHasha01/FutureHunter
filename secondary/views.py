from django.shortcuts import render
from .models import secondary


# Create your views here.

def index(request):
    a = secondary.objects.all()
    param = {'qurstion': a}
    return render(request, 'index.html', param)
