from django.contrib import admin
from .models import Movie, BookingTable

class MovieAdmin(admin.ModelAdmin):
    list_display = ('Movie_Id', 'Name', 'Release_date')
    list_display_links = ('Movie_Id', 'Name')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('Booking_Id', 'movie_name', 'show_date', 'show_time')
    list_display_links = ('Booking_Id',)



admin.site.register(Movie, MovieAdmin)
admin.site.register(BookingTable, BookingAdmin)

