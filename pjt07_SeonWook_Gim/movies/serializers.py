from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieTitleSerializer(many=True, read_only=True, source='movie_set')

    class Meta:
        model = Actor
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    actors = ActorNameSerializer(many=True, read_only=True)

    class ReviewSetSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)

    review_set = ReviewSetSerializer(many=True, read_only=True, source='reviews')
    
            
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)