from django.urls import path
from django.http import HttpResponse

def passeport_home(request):
    return HttpResponse("<h2>Service Passeport</h2><p>Aide pour démarches administratives.</p>")

urlpatterns = [
    path('', passeport_home),
]
