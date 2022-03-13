from django.shortcuts import render
from .models import Event

def my_projects(request):
    event = Event.objects.all()
    return render(request, 'myProjects/my_projects.html', {'event': event})
