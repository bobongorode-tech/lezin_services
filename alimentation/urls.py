from django.urls import path
from django.http import HttpResponse

def alimentation_home(request):
    return HttpResponse("<h2>Service Alimentation</h2><p>Produits alimentaires disponibles.</p>")

urlpatterns = [
    path('', alimentation_home),
]
