from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return render(request, 'landing/index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                user_login(request, user)
                return redirect("/home")
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('/login')

        else:
            return render(request, 'landing/login.html')


    
def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('/signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Exist')
                    return redirect('/signup')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email)
                    user.save()
                    print("user created")
                    user = authenticate(username = username, password = password)
                    if user is not None:
                        user_login(request, user)
                        return redirect("/settings")

            else:
                messages.info(request, 'Passwords Didn\'t Match')
                return redirect('/signup')



        return render(request, 'landing/signup.html')