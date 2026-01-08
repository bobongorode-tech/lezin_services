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
