from django.urls import path
from django.http import HttpResponse

def colis_home(request):
    return HttpResponse("<h2>Service Colis</h2><p>Suivi et envoi de colis.</p>")

urlpatterns = [
    path('', colis_home),
]
