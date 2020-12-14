from django.test import TestCase
from django.urls import reverse

from .models import Movie, BookingTable

class MoviePortalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(Movie_Id=1, Name='Movie-1', Release_date='2020-12-12')
        Movie.objects.create(Movie_Id=2, Name='Movie-2', Release_date='2020-12-13')

    def test_view_BookTicket(self):
        ## Test for checking if everything passed correctly.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertEqual(response.status_code, 200)
    
    def test_view_BookTicket_Incorrect_MovieID(self):
        ## Test for checking if an incorrect movie_id is passed in the link.
        url = reverse('BookTicket', args='5')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_BookTicket_Method_Changed(self):
        ## Test for checking if the HTTP method changed.
        url = reverse('BookTicket', args='1')
        response = self.client.get(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-15',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_BookTicket_Wrong_Date(self):
        ## Test for checking if wrong type of date data passed.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-32',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_BookTicket_Wrong_Time(self):
        ## Test for checking if wrong type of time data passed.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-19',
                                        'show_time' : '25:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)

    def test_view_BookTicket_Date_Key_Missing(self):
        ## Test for checking if the date key missing.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        #'show_date' : '2020-12-19',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_BookTicket_Time_Key_Missing(self):
        ## Test for checking if the time key missing.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-19',
                                        #'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_BookTicket_All_Key_Missing(self):
        ## Test for checking if both the date and time keys missing.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        #'show_date' : '2020-12-19',
                                        #'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    
    def test_view_BookTicket_Past_Date_Check(self):
        ## Test for if the date is already passed.
        url = reverse('BookTicket', args='1')
        response = self.client.post(url, 
                                    {
                                        'movie_name': Movie.objects.get(Movie_Id=1).Name,
                                        'show_date' : '2020-12-13',
                                        'show_time' : '15:00'
                                    }
                                    )
        self.assertNotEqual(response.status_code, 200)
    

