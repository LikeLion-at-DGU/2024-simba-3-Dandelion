import random, re
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from main.models import Category, Sutra, Talisman
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def split_text(text):
    # 마지막 부분 추출 (예: "- 법구경 116장 -")
    match = re.search(r"(- 법구경 \d+장 -)$", text)
    
    if match:
        last_phrase = match.group(1)
        main_text = text[:match.start()]
    else:
        last_phrase = ''
        main_text = text

    # 온점과 쉼표 기준으로 나누기 (구분자를 포함)
    chunks = re.split(r'([.,])', main_text)
    result_chunks = []
    for i in range(0, len(chunks) - 1, 2):
        result_chunks.append(chunks[i].strip() + chunks[i+1])
    
    # 마지막 구분자 뒤에 남아 있는 텍스트 처리
    if len(chunks) % 2 != 0:
        result_chunks.append(chunks[-1].strip())
    
    return result_chunks, last_phrase

@csrf_exempt
def past(request):
    if request.user.is_authenticated:
        return render(request, 'post/past.html')
    else:
        return redirect('accounts:login')

@csrf_exempt
def past_result(request):
    
    if Past.objects.filter(user=request.user).first() is None:
        Past.objects.create(user=request.user, category=Category.objects.get(id=1))

    past = Past.objects.filter(user=request.user).first()
    past.text = request.POST["user_text"]

    sutras = Sutra.objects.filter(category=1)
    if sutras.exists():
        sutra = random.choice(sutras)
        past.my_sutra = sutra.text
        past.user = request.user
        past.save()
        
        chunks, last_part = split_text(sutra.text)
    
        context = {
            'chunks': chunks,
            'last_part': last_part
        }

    return render(request, 'post/past_result.html', context)

@csrf_exempt
def start_108(request):
    return render(request, 'post/start_108.html')

@csrf_exempt
def init_108(request):
    
    sharedwish = MyWish.objects.get(user=request.user)
    sharedwish.num108_count = 0 # 0으로 초기화
    sharedwish.save()

    context = {
        'count' : 108 - sharedwish.num108_count
    }
    return render(request, 'post/do_108.html', context)

@csrf_exempt
def post_108(request):
    if request.method == 'POST':
        if MyWish.objects.filter(user=request.user).first() is None:
            MyWish.objects.create(user=request.user)

        post_108 = MyWish.objects.filter(user=request.user).first()
        post_108.title = request.POST['title']
        post_108.text = request.POST['text']
        
        post_108.save()  # 새로운 게시물 저장
        return redirect('post:init_108') 
    else:
        return render(request, 'post/post_108.html')
    
@csrf_exempt
def detail_108(request, id):
    my_wish = get_object_or_404(SharedWish, pk=id)  # 게시물 조회, 없으면 404 에러 발생
    return render(request, 'post/detail_108.html', {'wish' : my_wish})  # 템플릿에 게시물 전달

@csrf_exempt
def delete(request, id):
    # 로그인 여부 확인
    if not request.user.is_authenticated:
        return redirect('accounts:login')  # 로그인 페이지로 리디렉션

    delete_post = get_object_or_404(SharedWish, pk=id)

    # 권한 확인 (현재 사용자가 글쓴이인지 확인)
    if request.user == delete_post.user:
        delete_post.delete()
        return redirect('post:community_108')  # 삭제 후 커뮤니티 목록 페이지로 이동
    else:
        return redirect('post:detail_108', id=id)  # 권한이 없으면 해당 글 상세 페이지로 이동

@csrf_exempt
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

@csrf_exempt   
def do_108(request):

    mywish = MyWish.objects.filter(user=request.user).first()
    mywish.num108_count += 1
    mywish.save()
    if mywish.num108_count >= 108:
        return render(request, 'post/result_108.html')
    else:
        context = {
            'count' : 108 - mywish.num108_count
        }
        return render(request, 'post/do_108.html', context)

@csrf_exempt
def result_108(request):
    return render(request, 'post/result_108.html')

@csrf_exempt
def write_108(request):
    my_wish = MyWish.objects.get(user=request.user)
    SharedWish.objects.create(wish=my_wish)

    sharedwish = SharedWish.objects.all()
    return redirect('post:community_108')

@csrf_exempt
def community_108(request):
    sharedwish = SharedWish.objects.all()
    return render(request, 'post/community_108.html', {'sharedwishes' : sharedwish})

@csrf_exempt
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

@csrf_exempt
def talisman_end(request):
    talisman = Talisman.objects.get(user=request.user)
    category = talisman.talisman_category
    # 카테고리 번호를 입력 받아서 그대로 전달할 예정
    context = {
        'category' : category
    }
    return render(request, 'post/talisman_end.html', context)

@csrf_exempt
def future(request):
    if request.user.is_authenticated:
        return render(request, 'post/future.html')
    else:
        return redirect('accounts:login')

@csrf_exempt
def future_result(request):
    
    if Future.objects.filter(user=request.user).first() is None:
        Future.objects.create(user=request.user, category=Category.objects.get(id=2))

    future = Future.objects.filter(user=request.user).first()
    future.text = request.POST["user_text"]

    sutras = Sutra.objects.filter(category=2)
    if sutras.exists():
        sutra = random.choice(sutras)
        future.my_sutra = sutra.text
        future.user = request.user
        future.save()

        chunks, last_part = split_text(sutra.text)
    
        context = {
            'chunks': chunks,
            'last_part': last_part
        }
    return render(request, 'post/future_result.html', context)

