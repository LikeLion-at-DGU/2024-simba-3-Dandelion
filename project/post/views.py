import random
from django.shortcuts import render, redirect, get_object_or_404
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


def post_108(request):
    if request.method == 'POST':
        post_108 = SharedWish(
            title=request.POST['title'],
            user=request.user,
            text=request.POST['text']
        )
        post_108.save()  # 새로운 게시물 저장
        return render(request, 'post/do_108.html')  # 글쓰기 완료 후 do_108로 넘어감(do페이지 맞나요? + 5페이지라 하나 더 구성 해야함)
    else:
        return render(request, 'post/post_108.html')
    

def detail_108(request, id):
    my_wish = get_object_or_404(SharedWish, pk=id)  # 게시물 조회, 없으면 404 에러 발생
    return render(request, 'post/detail_108.html', {'wish' : my_wish})  # 템플릿에 게시물 전달

def delete(request, id):
    delete_post = SharedWish.objects.get(pk=id)

    delete_post.delete()
    return redirect('post:detail_108')


def likes(request, post_id):
    post = get_object_or_404(SharedWish, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()

    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('post:community_108', post.id)  # 좋아요 처리 후 커뮤니티 페이지에 계속 유지
    
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

def result_108(request):
    return render(request, 'post/result_108.html')

def community_108(request):
    sharedwish = SharedWish.objects.all()
    return render(request, 'post/community_108.html', {'wish' : sharedwish})

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
