from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeView(request, id):             # kontroller
    return render(request, "index.html")
    