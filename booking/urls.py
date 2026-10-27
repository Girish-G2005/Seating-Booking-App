from django.urls import path
from .views import get_booked_seats, book_seat

urlpatterns = [
    path('booked-seats/', get_booked_seats, name = 'booked-seats'),
    path('book-seat/', book_seat, name = 'book-seat'),
]