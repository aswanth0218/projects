from django.shortcuts import render
from .models import register

# Create your views here.


def register(request):
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        maxtable = register()
        maxtable.number1 = number1
        maxtable.number2 = number2
        maxtable.save()
    return render(request ,'register.html')


def approvel(request):
    result = register.object.value('num1' ,'num2').annotate(result=max('result'))
    return render(request,('approvel.html'),{'values':result})

