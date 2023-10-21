from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import  require_http_methods, require_safe, require_POST
from .models import Movie, Comment, Recomment
from .forms import MovieForm, CommentForm, RecommentForm

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


@login_required
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment_form.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)

@login_required
@require_http_methods(['POST'])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if movie.like_users.filter(pk=request.user.pk).exists():
                # if request.user in movie.like_users.all():
                movie.like_users.remove(request.user)
            else:
                movie.like_users.add(request.user)
            return redirect("movies:index")
        return redirect("accounts:login")
    
    
@login_required
@require_POST
def recomments_create(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    recomment_form = RecommentForm(request.POST)

    if recomment_form.is_valid():
        recomment = recomment_form.save(commit=False)
        recomment.movie = movie
        recomment.user = request.user
        recomment.comment = comment
        recomment_form.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'recomment_form': recomment_form,
    }
    return render(request, 'movies/detail.html', context)