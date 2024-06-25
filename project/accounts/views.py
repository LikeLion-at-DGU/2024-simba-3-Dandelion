from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST' :
        is_exist = User.objects.filter(username=request.POST['username'])
        if is_exist:
            #유저 이름이 이미 존재할 때
            return render(request, 'accounts/signup.html', {'error': '이미 사용중인 법명입니다.'})
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            user.save()
            auth.login(request, user)
            return render(request, 'main/mainpage.html')
    return render(request, 'accounts/signup.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/login.html', {'error': '아이디 혹은 비밀번호가 틀렸습니다. 다시 입력해주세요.'})
    else:
        return render(request, 'accounts/login.html')

@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect("main:mainpage")

