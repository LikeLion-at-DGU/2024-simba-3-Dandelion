import random
from django.shortcuts import render, redirect
from .models import *
from main.models import Category, Sutra
# Create your views here.
def past(request):
    if request.user.is_authenticated:
        return render(request, 'post/past.html')
    else:
        return redirect('accounts:login')

def past_result(request):
    
    past = Past()

    past.text = request.POST["user_text"]
    sutras = Sutra.objects.filter(category=1)
    if sutras.exists():
        sutra = random.choice(sutras)
        past.my_sutra = sutra
    past.user = request.user
    
    past.category = Category.objects.get(id=1) # 참회로 고정
    past.save()
    return render(request, 'post/past_result.html', {'past' : past})

def start_108(request):
    return render(request, 'post/start_108.html')

def init_108(request):
    
    sharedwish = SharedWish.objects.create(user=request.user)
    sharedwish.num108_count = 0 # 0으로 초기화
    sharedwish.save()

    context = {
        'count' : sharedwish.num108_count
    }
    return render(request, 'post/do_108.html', context)

def do_108(request):

    sharedwish = SharedWish.objects.filter(user=request.user, text="").first()
    sharedwish.num108_count += 1
    sharedwish.save()
    if sharedwish.num108_count >= 108:
         return render(request, 'post/result_108.html')
    else:
        context = {
            'count' : sharedwish.num108_count
        }
        return render(request, 'post/do_108.html', context)

def post_108(request):
    if request.method == 'POST':
        sharedwish = SharedWish.objects.filter(user=request.user, text="").first()
        sharedwish.text = request.POST["text"]
        sharedwish.save()

    return render(request, 'post/community.html') # 글 작성 후 커뮤니티 페이지로 이동

def community_108(request):
    return render(request, 'post/community.html')

def talisman(request): # POST 에 카테고리를 함께 전달
    if request.method == 'POST':
        pass
    else:
        return render(request, 'post/make_talisman.html')

def future(request):
    if request.user.is_authenticated:
        return render(request, 'post/future.html')
    else:
        return redirect('accounts:login')

def future_result(request):
    
    future = future()

    future.text = request.POST["user_text"]
    sutras = Sutra.objects.filter(category=2)
    if sutras.exists():
        sutra = random.choice(sutras)
        future.my_sutra = sutra
    future.user = request.user
    
    future.category = Category.objects.get(id=2) # 소망으로 고정
    future.save()
    return render(request, 'post/future_result.html', {'future' : future})