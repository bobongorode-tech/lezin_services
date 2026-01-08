from django.urls import path
from .views import location_home

urlpatterns = [
    path('', location_home, name='location_home'),
]
