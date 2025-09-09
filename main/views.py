from django.shortcuts import render

from main.models import Cars

# Create your views here.
def index(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'index.html', context)