from django.shortcuts import render
from .models import Event
from django.views.generic import DetailView

def my_projects(request):
    event = Event.objects.all()
    return render(request, 'myProjects/my_projects.html', {'event': event})

class ContinueProject(DetailView):
    model = Event
    template_name = 'myProjects/project_details.html'
    context_object_name = 'projects_str'

