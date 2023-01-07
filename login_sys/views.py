from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def register(request):
    if request.POST:
        username = request.POST['username']
        mail = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username not available!')
            return redirect('register')
        elif User.objects.filter(email=mail).exists():
            messages.info(request, 'email already used!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=mail,password=password)
            user.save();
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

