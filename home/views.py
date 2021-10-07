from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
import requests
from .models import Profile
from .forms import ProfileModelForm
API_KEY = '985d088b7d85476a9e834a2d8870b5b3'

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect('/')

def newspaper(request):
    if request.user.is_authenticated:
        url = 'https://newsapi.org/v2/everything?q=(india AND agriculture AND farmers AND bjp AND modi)&apiKey=' + API_KEY
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        context = {
            'articles': articles
        }
        return render(request, 'home/newspaper.html', context)
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
        obj = Profile.objects.get(user=request.user)

        context = {
            'obj': obj,
        }
        return render(request, 'home/profile.html', context)
                                   
    else:
        return redirect('/')

def logout_view(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('/')

def settings(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
        done = False

        if form.is_valid():
            form.save()
            return redirect('/profile')

        context = {
            'form': form,
            'done': done,
        }
        return render(request, 'home/settings.html', context)
    else:
        return redirect('/')