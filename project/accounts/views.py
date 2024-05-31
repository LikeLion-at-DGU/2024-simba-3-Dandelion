from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is None:
            user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        user.save()

        auth.login(request,user)
        return redirect("main:mainpage")
    
    return render(request, 'accounts/signup.html')