from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('location/', include('location.urls')),
    path('sante/', include('sante.urls')),
    path('alimentation/', include('alimentation.urls')),
    path('colis/', include('colis.urls')),
    path('passeport/', include('passeport.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ta page d'accueil
    path('sante/', views.maintenance, name='sante'),
    path('colis/', views.maintenance, name='colis'),
    path('alimentation/', views.maintenance, name='alimentation'),
    path('passeport/', views.maintenance, name='passeport'),
]
