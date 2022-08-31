import random
from django.shortcuts import render

# Create your views here.
def index(request):
    # print(dir(request))
    # print(request.user)
    # template을 return
    # return render(request, 'templates/articles/index.html')
    return render(request, 'articles/index.html')

def greeting(request):
    name = 'Alice'
    foods = ['파스타', '짬뽕', '비빔밥']

    context = {
        'name': name,
        'foods': foods
    }
    return render(request, 'articles/greeting.html', context)

# 저녁메뉴 추천 view 함수 생성
def dinner(request):
    # 저녁메뉴 목록
    dinner = ['짜장', '짬뽕', '탕수육']
    # 저녁 메뉴 목록중에 무작위 요소 하나 선택
    pick = random.choice(dinner)
    # 저녁 메뉴와 선택된 메뉴 dict에 담아서

    wallet = []

    context = {
        'dinner': dinner,
        'pick': pick,
        'wallet': wallet
    }
    # dinner.html에 넘겨주기
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(dir(request))
    print(request.GET)
    print(request.GET.get('username'))
    username = request.GET.get('username')
    context = {
        'username': username
    }
    return render(request, 'articles/catch.html', context)

def profile(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/profile.html', context)