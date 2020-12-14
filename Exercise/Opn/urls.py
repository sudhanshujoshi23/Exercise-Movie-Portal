from django.urls import path
from . import views


urlpatterns = [

    path('movies/<int:id>/Book', views.BookTicket, name='BookTicket'),
    path('Cancel/<int:id>', views.CancelTicket, name='CancelTicket'),
    path('Reschedule/<int:id>', views.Reschedule, name='Reschedule'),   

]