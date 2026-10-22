from django.urls import path
from .views import booked_seats

urlpatterns = [
    path('booked-seats/', booked_seats, name = 'booked-seats'),
]