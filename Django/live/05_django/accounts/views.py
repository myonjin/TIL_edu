
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
         #로그인
            auth_login(request, form.get_user()) #request,유저정보
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    #로그아웃
    auth_logout(request)
    return redirect('articles:index')   

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          #회원가입후 곧바로 로그인 진행
            auth_login(request, user)
            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    # auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)# 기존 유저 
    context = {
        'form' : form,
    }
    return render(request,'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':  # 로그아웃이 되어버림  그래서 가지고있는 세션을 업데이트 해줘야함 새로운 패스워드에
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')
    else:
        form =PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)