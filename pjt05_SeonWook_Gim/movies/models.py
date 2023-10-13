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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(max_length=100, choices=MOVIE_CHOICES, null="CM", default="Comedy")
    score = models.FloatField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)