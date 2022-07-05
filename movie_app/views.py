from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Max, Min, Count, Avg


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


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie,
    }
    return render(request, 'movie_app/one_movie.html', context=data)
