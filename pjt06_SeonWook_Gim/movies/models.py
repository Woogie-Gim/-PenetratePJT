from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    MOVIE_CHOICES = (
        ('Comedy', 'Comedy'),
        ('Fantansy', 'Fantansy'),
        ('Romance', 'Romanace'),
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(max_length=100, choices=MOVIE_CHOICES, null="CM", default="Comedy")
    score = models.FloatField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')


class Comment(models.Model):
    movie = models.ForeignKey(Movie, default=1, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(null=True, default='', max_length=250)


class Recomment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
                             on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, default=1, on_delete=models.CASCADE)
    content = models.CharField(null=True, default='', max_length=250)