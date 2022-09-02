import re
from django.shortcuts import render, redirect
from .models import Movie
genre_list=['코미디','액션','스릴러']

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, "movies/index.html",context)

def new(request):
    
    context ={
        'genre_list': genre_list,
    }
    return render(request, 'movies/new.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        audience = request.POST.get('audience')
        release = request.POST.get('release_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(title = title, audience = audience, release_date = release, genre = genre, score =score, poster_url= poster_url, description=description )
        movie.save()
    return redirect('movies:detail', movie.pk)

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    
    movie = Movie.objects.get(pk=movie_pk)

    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    
    return redirect('movies:detail', movie.pk)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
    return redirect('movies:index')
    