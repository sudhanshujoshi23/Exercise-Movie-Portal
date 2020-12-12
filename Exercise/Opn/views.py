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
        try:
            day = request.POST['show_date']
            time = request.POST['show_time']
            datetime.datetime.strptime(day, '%Y-%m-%d')
            datetime.datetime.strptime(time, '%H:%M')   
        except:
            return HttpResponseBadRequest("BAD REQUEST")
        if datetime.datetime.strptime(day, '%Y-%m-%d') < datetime.datetime.now():
            return HttpResponseBadRequest("You cannot select a previous date for booking tickets.")

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
    booking = get_object_or_404(BookingTable, Booking_Id = id)
    try:
        day = request.POST.get('show_date')
        time = request.POST.get('show_time')
        datetime.datetime.strptime(day, '%Y-%m-%d')
        datetime.datetime.strptime(time, '%H:%M')
    except:
        return HttpResponseBadRequest("BAD REQUEST")

    if datetime.datetime.strptime(day, '%Y-%m-%d') < datetime.datetime.now():
            return HttpResponseBadRequest("You cannot select a previous date for booking tickets.") 

    booking.show_date = day
    booking.show_time = time
    booking.save()
    return HttpResponse('Booking Rescheduled.')







