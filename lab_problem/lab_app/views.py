from django.shortcuts import render
from .models import Numbers

# Create your views here.
def home(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        sum_result = num1 + num2
        return render(request, 'result.html', {'sum_result': sum_result})
    return render(request, 'home.html')     