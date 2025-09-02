from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
 return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
 return HttpResponse("<h1>A propos </h1>")

def contact(request):
 return HttpResponse("<p> Contact </p>")