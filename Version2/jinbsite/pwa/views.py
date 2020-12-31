from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request,"pwa/home.html")


def resources(request):

    return render(request,"pwa/resources.html")

def contact(request):

    return render(request,"pwa/contact.html")