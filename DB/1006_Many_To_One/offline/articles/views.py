import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    # path 함수에 views.index 함수 정보 넘겨 주면서
    # path 함수 내부에서 호출할때 첫번째 인자 넘겨준다

    articles = Article.objects.all()
    context = {
        'articles':articles
    }

    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.user.is_authenticated:
    # 사용자가 POST 요청보내면 게시글 생성 해준다
        if request.method == 'POST':
            # 사용자가 POST 요청을 보낼때 같이 보낸 정보들
            # model에 대한 정보와 form에 대한 정보 모두 가지고있는
            # ArticleForm 에게 사용자의 요청 정보를 같이 넘겨줘서 

            form = ArticleForm(request.POST)
            #사용자가 보낸 정보가 정상적인지
            if form.is_valid():

                article=form.save(commit=False)
                article.user = request.user
                article.save()
            
                return redirect('articles:index')

        else:
            form = ArticleForm()
        context ={
            'form': form
        }

        return render(request, 'articles/create.html', context)
    return redirect('accounts:login')

def detail(request , article_pk):
    # article_pk의 article 값들 담겨있음 article.title article.pk 등

    article = Article.objects.get(pk=article_pk)

    # 역참조
    comment = article.comment_set.all()
    form = CommentForm()
    context={
        'article':article,
        'form':form,
        'comment':comment
    }
    return render(request, 'articles/detail.html', context)

def comment_create(request,article_pk):
    # article_id 찾기
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #comment 객체 생성 
            # 저장해서 생성하는데 저장은안되게 FALSE 
            comment = form.save(commit=False)
            comment.article = article
            comment.save() # db에 값을 집어넣는다 
    return redirect('articles:detail', article_pk)

@require_POST


def delete(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.user == request.user:
            article.delete()
        return redirect('articles:index')
    
    return redirect('accounts:login')