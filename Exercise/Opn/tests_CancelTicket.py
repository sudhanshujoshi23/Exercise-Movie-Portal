from django.test import TestCase
from django.urls import reverse

from .models import Movie, BookingTable

class MoviePortalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(Movie_Id=1, Name='Movie-1', Release_date='2020-12-12')
        Movie.objects.create(Movie_Id=2, Name='Movie-2', Release_date='2020-12-13')
        BookingTable.objects.create(Booking_Id=1, movie_name='Movie-1', show_date='2020-12-18', show_time='15:00')
        BookingTable.objects.create(Booking_Id=2, movie_name='Movie-2', show_date='2020-12-18', show_time='17:00')

    def test_view_CancelTicket(self):
        ## Test for checking if correct Booking ID passed.
        url = reverse('CancelTicket', args='1')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
    
    def test_view_CancelTicket_Incorrect_BookingID(self):
        ## Test for checking if incorrect Booking ID passed.
        url = reverse('CancelTicket', args='5')
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_CancelTicket_Method_Changed(self):
        ## Test for checking if the HTTP method is changed.
        url = reverse('CancelTicket', args='1')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)