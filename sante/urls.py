from django.urls import path
from django.http import HttpResponse

def sante_home(request):
    return HttpResponse("<h2>Service Santé</h2><p>Conseils et assistance médicale.</p>")

urlpatterns = [
    path('', sante_home),
]
