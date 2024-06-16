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