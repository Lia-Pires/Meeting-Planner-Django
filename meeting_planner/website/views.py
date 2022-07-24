from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime





def welcome(request):
    return render(request, 'website/home.html', {"message" : "Transmitings From The View Function"})


def date(request):
    return HttpResponse(f"{str(datetime.now())}")


def about(request):
    return HttpResponse("My name is Lia")


