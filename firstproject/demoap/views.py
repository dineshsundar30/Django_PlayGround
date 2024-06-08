from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse("Hi welcome to my first projct")

def contact(request):
    return HttpResponse("Dineshkumar S\ndharmapuri")

def contact_num (request, phone_num):
    return HttpResponse(f"your contact num is {phone_num}")

def newurl(request):
    return HttpResponse("this is new_url")

def oldurl(request):
    return redirect("newurl")

def oldurl2(request):
    return reverse(redirect("demoap:new_url"))