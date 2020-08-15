from django.shortcuts import render
from .models import  Project

# Create your views here.

def home(request):
    Pro = Project.objects.all()
    return render (request,  'html_files/home.html', {'key': Pro})