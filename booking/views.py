from django.contrib.auth.models import User
from .models import CurrentBookings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import CurrentBookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def booked_seats(request):
    bookedSeats = CurrentBookings.objects.all()
    bookedSerializer = CurrentBookingSerializer(bookedSeats, many=True)
    return Response(bookedSerializer.data, status = status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes(['IsAuthenticated'])
def book_seat(request):
    table_no = request.data.get('table_no')
    seat_no = request.data.get('seat_no')

    if table_no is None or seat_no is None:
        return Response({'error': 'Table number and Seat number are required.'}, status = status.HTTP_400_BAD_REQUEST)