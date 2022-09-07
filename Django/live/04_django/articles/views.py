from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)




# def create(request):
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         # print('aaaaaaaaaaaaaaa')
#         # print(form)
#         # print('aaaaaaaaaaaaaaa')
#         # print(form.data.get('title'))
#         # print('aaaaaaaaaaaaaaa')
#         # print(form.title)
#         # print('aaaaaaaaaaaaaaa')
#         if form.is_valid():
#             # print(form.data)
#             # print(type(form.data))
            
#             # print(form.data['title'])
#             title = form.data.get('title')
#             content = form.data.get('content')
#             article = Article(title=title,content=content)
#             article.save()
#             return redirect('articles:detail',article.pk)
#     form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request,'articles/create.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method =='POST': 
        #create
        form = ArticleForm(request.POST)
        print(form)
        print(form.title)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        #New
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)





@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST': #require 있으면 삭제가능
        article.delete()
        return redirect('articles:index')
    return redirect('articles/detail', article.pk) #require 있으면 삭제가능


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)

@require_http_methods(['GET','POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)


    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
   