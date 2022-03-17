from django.shortcuts import render

def home(request):
    return render(request, 'aboutMy/home.html')

def contacts(request):
    return render(request, 'aboutMy/contacts.html')
