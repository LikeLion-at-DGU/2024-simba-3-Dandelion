from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create your views here.
=======
# Create your views here.
def signup(request):
    if request.method == 'POST' :
        is_exist = User.objects.filter(username=request.POST['username'])
        if is_exist:
            #유저 이름이 이미 존재할 때
            return render(request, 'accounts/signup.html')
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            user.save()
            auth.login(request, user)
            return render(request, 'main/mainpage.html')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("main:mainpage")
        else:
            return render(request, "accounts/signup.html")
        
    elif request.method == 'GET' :
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect("main:mainpage")

>>>>>>> cc93022112c7dceb2811903372a0ab470e492c4e
