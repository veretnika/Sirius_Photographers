from django.shortcuts import render
# from .models import Task
# from django.http import HttpResponse


def index(request):
    # tasks = Task.objects.all()
    return render(request, 'personalArea/index.html')


# def photographer(request):
#     return render(request, 'main/photographer.html')