from rest_framework.serializers import ModelSerializer
from .models import Movies,Shows,Seats

class Movie_Serializer(ModelSerializer):
    class Meta:
        model = Movies
        fields ='__all__'


class Seats_Serializer(ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'


class Shows_Serializer(ModelSerializer):
    class Meta:
        model = Shows
        fields = '__all__'