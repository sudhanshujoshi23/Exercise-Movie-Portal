from django.db import models
from datetime import datetime


class Movie(models.Model):
    Movie_Id = models.AutoField(primary_key=True, auto_created=True)
    Name = models.CharField(max_length=100)
    Release_date = models.DateField('Release Date')

    def __str__(self):
        return f"('{self.Movie_Id}', '{self.Name}')"


class BookingTable(models.Model):
    Booking_Id = models.AutoField(primary_key=True, auto_created=True)
    movie_name = models.CharField(max_length=100)
    show_date = models.DateField()
    show_time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"('{self.Booking_Id}', '{self.movie_name}, {self.show_date}, {self.show_time}')"


    



