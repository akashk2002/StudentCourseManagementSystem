from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return HttpResponse("PFSD SDP PROJECT")

def demofunction1(request):
    return HttpResponse("<h2>PFSD SDP PROJECT</h2>")

def homefuction(request):
    return render(request, "index.html")

def aboutfuction(request):
    return render(request, "about.html")

def contactfuction(request):
    return render(request, "contact.html")

def loginfuction(request):
    return render(request, "login.html")