from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie.models import Director, Review, Movie
from movie.serializers import *

@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data_dict = DirectorSerializer(directors, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        product = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    data_dict = DirectorSerializer(product).data
    return Response(data=data_dict)



@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data_dict = MovieSerializer(movies, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Category not found'},status=status.HTTP_404_NOT_FOUND)
    data_dict = MovieSerializer(movie).data
    return Response(data=data_dict)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data_dict = Review(reviews, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    data_dict = ReviewSerializer(review).data
    return Response(data=data_dict)