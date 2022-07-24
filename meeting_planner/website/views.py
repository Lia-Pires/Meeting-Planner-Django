from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting # type: ignore





def welcome(request):
    return render(request, 'website/home.html', {"num_meetings" : Meeting.objects.count()})


def date(request):
    return HttpResponse(f"{str(datetime.now())}")


def about(request):
    return HttpResponse("My name is Lia")


