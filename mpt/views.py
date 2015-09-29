from django.shortcuts import render
from models import *


def home_info(request):
    info = HomePage.objects.all()
    return render(request, r'mpt\home.html', {'info': info[0]})
