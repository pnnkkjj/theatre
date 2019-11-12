from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    category = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return "{}--{}".format(self.movie_name,self.language)

    def __repr__(self):
        return str(self)

    class Meta:
        db_table = 'movies'
        verbose_name_plural = "Movies"


class Seats(models.Model):
    seat_no = models.IntegerField(primary_key=True)
    price = models.FloatField(null=False)

    def __str__(self):
        return "{}->{}".format(self.seat_no,self.price)

    def __repr__(self):
        return str(self)

    class Meta:
        db_table = "seats"
        verbose_name_plural = "Seats"


class Shows(models.Model):
    showtime = models.DateTimeField(null=False)
    screen = models.CharField(max_length=15)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='shows')
    seats = models.ManyToManyField(Seats)

    def __str__(self):
        return "{} -> {}".format(self.showtime,self.screen)

    def __repr__(self):
        return str(self)

    class Meta:
        db_table="shows"
        verbose_name_plural = 'Shows'


