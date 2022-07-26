from django.shortcuts import render
from datetime import datetime
from meetings.models import Meeting 
from django.http import HttpResponse


def welcome(request):
    return render(request, 'website/home.html', {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")


def about(request):
    return HttpResponse("My Name is Lia Pires")
