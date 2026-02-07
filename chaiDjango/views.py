from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello home")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello about")

def contact(request):
    return HttpResponse("Hello contact")