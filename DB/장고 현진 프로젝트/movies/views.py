from contextlib import redirect_stderr
from django.shortcuts import render, redirect

from movies.forms import MovieForm
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form
    }
    
    return render(request, 'movies/create.html', context)
    

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'movie' : movie
    }
    return render(request,'movies/detail.html',context)
    

def update(request,movie_pk):
    movie= Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST , instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm(instance=movie)
    context={
        'form':form,
        'movie':movie
    }
    
    return render(request,'movies/update.html',context)
    

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
    return redirect('movies:index')




