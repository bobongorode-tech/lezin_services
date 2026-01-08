from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def maintenance(request):
    return render(request, 'maintenance.html')
