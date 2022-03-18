from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_projects, name='my_projects'),
    path('<int:pk>', views.ContinueProject.as_view(), name='project-details')
]
