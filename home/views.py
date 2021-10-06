from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect('/')

def newspaper(request):
    if request.user.is_authenticated:
        return render(request, 'home/newspaper.html')
    else:
        return redirect('/')

def marketplace(request):
    if request.user.is_authenticated:
        return render(request, 'home/marketplace.html')
    else:
        return redirect('/')

def notifications(request):
    if request.user.is_authenticated:
        return render(request, 'home/notifications.html')
    else:
        return redirect('/')

def profile(request):
    if request.user.is_authenticated:                            
        return render(request, 'home/profile.html', context)
    else:
        return redirect('/')

def logout_view(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('/')

def settings(request):
    if request.user.is_authenticated:
        return render(request, 'home/settings.html')
    else:
        return redirect('/')