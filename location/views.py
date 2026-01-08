from django.shortcuts import render

def location_home(request):
    return render(request, 'location/location_home.html')
