from django.shortcuts import render

# Create your views here.
from landing import views

def landing(request):
    return render(request, "landing/index.html")