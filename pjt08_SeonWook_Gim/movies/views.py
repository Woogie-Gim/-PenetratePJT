from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.db.models import F


# Create your views here.
@require_safe
def index(request):
    sort_by = request.GET.get('sort_by', 'popularity')
    sort_order = request.GET.get('sort_order', 'asc')

    movies = Movie.objects.all()

    sort_field = sort_by if sort_order == 'asc' else F(sort_by).desc(nulls_last=True)

    movies = movies.order_by(sort_field)

    genres = Genre.objects.filter(movie__in=movies)

    context = {
        'movies': movies,
        'genres': genres,
        'sort_by': sort_by,
        'sort_order': sort_order,
    }

    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre = movie.genres.all()
    context = {
        'movie': movie,
        'genre': genre,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request, genre):
    movies = Movie.objects.all()

    context = {
        'movies': movies,
        'genre': genre,
    }
    return render(request, 'movies/recommended.html', context)


