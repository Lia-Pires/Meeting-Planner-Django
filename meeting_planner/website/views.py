from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime




def welcome(request):
    return HttpResponse('Welcome to the Meeting Planner')


def date(request):
    return HttpResponse(f'{str(datetime.now())}')


