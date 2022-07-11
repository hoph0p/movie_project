from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg
from django.http import HttpResponse


# Create your views here.
def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    data = {
        'movies': movies,
        'agg': agg,
        'total': movies.count(),
    }
    return render(request, 'movie_app/all_movies.html', context=data)


def show_all_directors(request):
    directors = Director.objects.all()
    data = {
        'directors': directors
    }
    return render(request, 'movie_app/all_directors.html', context=data)

def show_all_actors(request):
    actors = Actor.objects.all()
    data = {
        'actors': actors
    }
    return render(request, 'movie_app/all_actors.html', context=data)


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie,
    }
    return render(request, 'movie_app/one_movie.html', context=data)


def show_one_director(request, id: int):
    director = get_object_or_404(Director, id=id)
    data = {
        'director': director
    }
    return render(request, 'movie_app/one_director.html', context=data)


def show_one_actor(request, id: int):
    actor = get_object_or_404(Actor, id=id)
    data = {
        'actor': actor
    }
    return render(request, 'movie_app/one_actor.html', context=data)
