from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse('Welcome to the meeting planner application')


def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")

def about (request):
    return HttpResponse("My name is Lia")

