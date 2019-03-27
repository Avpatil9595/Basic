from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.


def show(request):

    context={'form':SkillForm()}
    return render(request,"show.html",context)
    # return HttpResponse('Hi this is index page.')

