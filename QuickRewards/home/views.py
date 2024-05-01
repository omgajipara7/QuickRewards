from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("my name is om")
def forpath(request):
    return HttpResponse("for giving path")

def index(request):
    return render(request,"htmlfiles/index.html")
def about(request):
    return render(request,"htmlfiles/about.html")

def redirect_to_about(request):
    return redirect('about')
