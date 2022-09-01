from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 사용자의 모든 요청 정보가 첫번쨰 인자로 전달된다.
def index(request):
    # Class.manager.QuerySet API
    # Article.objects.내가 보낼 요청
    # all() -> 함수 호출
    # 함수호출? return 값이 있다.
    articles = Article.objects.all()[::-1]
    context = {
        'articles': articles
    }
    # view 함수의 일은
    # 사용자 request에 대한 response이며,
    # 일반적으로 그 응답은 html과 같은 문서를 보내주는 일이다.
    # django MTV design pattern
    # T = template
    # templates 폴더는 모든 app들이 동일한 이름으로 사용하고 있다.
    # 같은 경로가 만들어지게 된다.
    # pages/templates/index.html
    # articles/templates/index.html
    # return render(request, 'templates/articles/index.html')
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자가 요청할떄 보낸
    # GET 방식으로 요청하면서 보낸 정보를 가져와야한다.
    # 사용자요청정보를 담고있는 request의 GET 이라고 하는 곳에 담겨있다.
    # key:value형태로 key = input tag name attrs
    title = request.POST.get('title') # input value
    content = request.POST.get('content') 
    # print(dir(request))
    # print(request.POST)
    # title과 content에 해당하는 게시글을 생성
    article = Article()
    # article 객체의 title 속성에 사용자가 입력한 제목을 담는다.
    article.title = title
    article.content = content
    # --- 이전까지는 그냥 python ---
    # db에 반영하는 행위 save() 메서드가 해줄것이다.
    article.save()

    '''
    두번째 방법
    article = Article(title=title, content=content)
    article.save()

    세번째 방법
    Article.objects.create(title=title, content=content)
    '''
    # return render(request, 'articles/index.html')
    # 내가 할일 게시글 생성은 끝이 났으니...
    # 나는 index페이지를 보여주는 view함수에게 일을 맡길 것이다...
    # app_name:path_name
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def detail(request, article_pk):
    # article_pk 번에 해당하는 게시글을 뽑아서 그 정보를 넘겨준다.
    # get() querySet API는 정확하게 하나의 정보만 받아올 수 있도록
    # 조건을 달아주어야 한다.
    # Article.objects.get(title='제목') # 중복될 수 있는 조건을 달면 안된다
    article = Article.objects.get(pk=article_pk) # 하나만 가지고 올거니까
    print(article.pk)
    print(article.title)
    print(article.content)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    # print(dir(request))
    # print(request.method)
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        # 삭제 해달라는 요청에 맞춰서 게시글을 삭제했다.
    return redirect('articles:index')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 게시글 생성과 다른점은
    # 게시글 생성은 새로운 article 객체 생성 article = Article()
    # 게시글 수정은 기존 DB에서 article 정보 받아와서 수정
    article = Article.objects.get(pk=article_pk)
    # 특정 pk에 해당하는 article 가지고 와서 수정
    article.title = title
    article.content = content
    article.save() # update view funcion 할일 끝
    # 사용자에게는 html 문서 보내줘야한다.
    # 근데 내가 하진 않음
    return redirect('articles:detail', article.pk)