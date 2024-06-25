from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        is_exist = User.objects.filter(username=request.POST['username']).exists()
        if is_exist:
            # 유저 이름이 이미 존재할 때 에러 메시지 전달
            return render(request, 'accounts/signup.html', {'error': '중복입니다. 다른 법명을 입력해주세요.'})
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            user.save()
            auth.login(request, user)
            return redirect('main:mainpage')
    return render(request, 'accounts/signup.html')


# def login(request):
#     if request.method == 'POST' :
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(request, username=username, password=password)
        
#         if user is not None:
#             auth.login(request,user)
#             return redirect("main:mainpage")
#         else:
#             return render(request, "accounts/signup.html")
        
#     elif request.method == 'GET' :
#         return render(request, 'accounts/login.html')
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
            return render(request, 'accounts/login.html', {'error': '아이디나 비밀번호가 틀렸습니다. 다시 입력해주세요.'})
    else:
        return render(request, 'accounts/login.html')


@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect("main:mainpage")

