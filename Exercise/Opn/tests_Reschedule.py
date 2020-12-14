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

    def test_view_Reschedule(self):
        ## Test for checking if everything passed correctly.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        'show_time' : '19:00'
                                    }
                                    )
        self.assertEqual(response.status_code, 200)
    
    def test_view_Reschedule_Date_Change(self):
        ## Test for checking if only the date is changed.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        #'show_time' : '19:00'
                                    }
                                    )
        self.assertEqual(response.status_code, 200)

    def test_view_Reschedule_Time_Change(self):
        ## Test for checking if only the date is changed.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        #'show_date' : '2020-12-15',
                                        'show_time' : '19:00'
                                    }
                                    )
        self.assertEqual(response.status_code, 200)
    
    def test_view_Reschedule_Incorrect_BookingID(self):
        ## Test for checking if an incorrect booking_id is passed in the link.
        url = reverse('Reschedule', args='5')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_Reschedule_Method_Changed(self):
        ## Test for checking if the HTTP method changed.
        url = reverse('Reschedule', args='1')
        response = self.client.get(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_Reschedule_Wrong_Date(self):
        ## Test for checking if wrong type of date data passed.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-32',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_Reschedule_Wrong_Time(self):
        ## Test for checking if wrong type of time data passed.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-19',
                                        'show_time' : '25:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)

    
    
    def test_view_Reschedule_Both_Key_Missing(self):
        ## Test for checking if both the date and time keys missing.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        #'show_date' : '2020-12-19',
                                        #'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_Reschedule_Past_Date_Check(self):
        ## Test for if the date is already passed.
        url = reverse('Reschedule', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-13',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    

