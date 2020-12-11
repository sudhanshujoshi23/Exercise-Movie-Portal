from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Movie, BookingTable
import datetime
from django.views.decorators.http import require_http_methods



@require_http_methods(request_method_list=['POST'])
def BookTicket(request, id):
    movies = get_object_or_404(Movie, Movie_Id = id)
    if movies:
        name = movies.Name
        day = request.POST['show_date']        
        time = request.POST['show_time']
        booking = BookingTable(movie_name=name, show_date=day, show_time=time)
        booking.save()
    return HttpResponse('Booking Confirmed.')

@require_http_methods(request_method_list=['DELETE'])
def CancelTicket(request, id):
    booking = get_object_or_404(BookingTable, Booking_Id = id)
    if booking:
        booking.delete()
    return HttpResponse('Booking Cancelled.')

@require_http_methods(request_method_list=['POST'])
def Reschedule(request, id):
    booking = BookingTable.objects.get(Booking_Id = id)
    if booking:
        booking.show_date = request.POST.get('show_date')
        booking.show_time = request.POST.get('show_time')
    booking.save()
    return HttpResponse('Booking Rescheduled.')







