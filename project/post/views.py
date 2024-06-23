import random
from django.shortcuts import render, redirect
from .models import *
from main.models import Category, Sutra, Talisman
import time
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
         return render(request, 'post/ing_108.html')
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

        return redirect(request, 'post:init_108') # 글 작성 후 do_108 페이지로 이동
    else:
        return render(request, 'post/post_108.html')

def result_108(request):
    return render(request, 'post/result_108.html')

def community_108(request):
    sharedwish = SharedWish.objects.all()
    return render(request, 'post/community.html', {'wish' : sharedwish})

def talisman(request): # POST 에 카테고리를 함께 전달
    if request.method == 'POST':
        if Talisman.objects.filter(user=request.user).first() is None:
            Talisman.objects.create(user=request.user)
            
        talisman = Talisman.objects.filter(user=request.user).first()
        talisman.talisman_category = request.POST['category']
        talisman.save()
        context = {
            'talisman' : talisman
        }
        return render(request, 'post/talisman_ing.html', context)
    else:
        return render(request, 'post/talisman_post.html')

def talisman_end(request):
    talisman = Talisman.objects.get(user=request.user)
    category = ""
    # 카테고리 번호를 입력 받아서 그대로 전달할 예정
    context = {
        'category' : category
    }
    return render(request, 'post/talisman_end.html', context)

def future(request):
    if request.user.is_authenticated:
        return render(request, 'post/future.html')
    else:
        return redirect('accounts:login')

def future_result(request):
    
    future = Future()

    future.text = request.POST["user_text"]
    sutras = Sutra.objects.filter(category=2)
    if sutras.exists():
        sutra = random.choice(sutras)
        future.my_sutra = sutra
    future.user = request.user
    
    future.category = Category.objects.get(id=2) # 소망으로 고정
    future.save()
    return render(request, 'post/future_result.html', {'future' : future})
