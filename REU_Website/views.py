from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def mentors(request):
    return render(request, 'mentors.html')

def flyer(request):
    return render(request, 'flyer.html')