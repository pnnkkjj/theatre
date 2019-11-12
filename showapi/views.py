from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Movies,Seats,Shows
from .serializers import Movie_Serializer,Seats_Serializer,Shows_Serializer
# Create your views here.


class Movie_Views(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = Movie_Serializer


class Seat_views(ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = Seats_Serializer


class Show_Views(ModelViewSet):
    queryset = Shows.objects.all()
    serializer_class = Shows_Serializer

    
