from django.urls import path
from .views import windata

urlpatterns = [
    path('value/',windata, name='data-available'),
]