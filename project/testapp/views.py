from django.shortcuts import render

# Create your views here.
def past (request):
    return render(request, 'main/frame8.html')


def page2 (request):
    return render(request, 'main/page2.html')

def page5 (request):
    return render(request, 'main/page5.html')

def page6 (request):
    return render(request, 'main/page6.html')

def page7 (request):
    return render(request, 'main/page7.html')

# past가 함수의 이름이 되게 됨, urls.py에서 두 번째에 past라고 써주면 됨. main/frame8.html에서 main/은 main이라는 큰 범위 안에서 접근하겠다는 의미임.