from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/vie-deli.html')

def profile(request):
    return render(request, 'pages/profile.html')

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})


def vie_deli(request):
    return render(request, 'pages/vie-deli.html')

def tu_nho(request):
    return render(request, 'pages/tu-nho.html')

def mona_hotel(request):
    return render(request, 'pages/mona-hotel.html')