from django.shortcuts import render
from .models import windata

# Create your views here.
def data_available(request):
    valid_data = windata.objects.all()
    max_datapoint = windata.objects.all()
    find_value = valid_data / max_datapoint * 100
    print(find_value)

def store_value(request):
    store = find_value.objects.all()
