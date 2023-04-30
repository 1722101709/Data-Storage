from django.shortcuts import render
from django.http import HttpResponse
from .models import Dst


def home(request):
    return HttpResponse("<h1>Data Storage Application</h1>")


def data(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        area = request.POST['area']
        gender = request.POST['gender']
        otp = request.POST['otp']
        entry = request.POST['entry']
        flag = True if otp == entry else False
        flag2 = not flag
        if flag == True:
            Dst.objects.create(name=name, age=age, area=area, gender=gender)
        data = {'name': name, 'age': age, 'area': area, 'gender': gender} if flag == False else {}
        data.update({'flag': flag, 'flag2': flag2})
        return render(request, 'data.html', data)
    else:
        return render(request, 'data.html')


