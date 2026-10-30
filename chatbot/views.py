from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import get_available_seat_count, get_jarvis_response
from .intents import Intent, get_intent

# API endpoint to handle chat messages and return the detected intent
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    message = request.data.get('message', '')

    if not message:
        return Response({'error': 'Message is required'}, status = status.HTTP_400_BAD_REQUEST)

    intent = get_intent(message)

    if intent == Intent.CHECK_AVAILABILITY:
        available_seats = get_available_seat_count()

        return Response({'reply': f"There are {available_seats} seats available."}, status = status.HTTP_200_OK)


