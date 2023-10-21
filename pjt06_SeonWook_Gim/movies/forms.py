from django import forms
from .models import Movie, Comment, Recomment

class MovieForm(forms.ModelForm):
    score = forms.FloatField(
      max_value=5,
      min_value=0,
      widget= forms.NumberInput(attrs={"step": 0.5}))    
    class Meta:
        model = Movie
        fields = ('title', 'description', 'genre', 'score', 'image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ('content',)