from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    return render(request, 'about.html')


def home(request):
    return HttpResponse('<html><title> Home | Kukuh Primadito</titlle></html>')
