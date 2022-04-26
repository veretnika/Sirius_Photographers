from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page site', 'tasks': tasks})


def photographer(request):
    return render(request, 'main/photographer.html')


def top_photographers(request):
    return render(request, 'main/top_Photographers.html')


def regulations(request):
    return render(request, 'main/regulations.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def donation(request):
    return render(request, 'main/donation.html')

# добавить остальные функции