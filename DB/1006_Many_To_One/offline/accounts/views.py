from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustumUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustumUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user )
        
            return redirect('articles:index')
    else:
        form = CustumUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
            # return redirect('articles:index')

    else:
        form = AuthenticationForm()
    context ={
        'form' : form
    }
    return render(request,'accounts/login.html',context)