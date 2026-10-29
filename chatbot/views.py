from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import get_jarvis_response

# Create your views here.

@api_view(['POST'])
@permission_classes(['IsAuthenticated'])
def chat(response):
    message = response.data.get("message", "").strip()

    if not message:
        return Response({'error': 'Message is required.'}, status = status.HTTP_400_BAD_REQUEST)

    try:
        reply = get_jarvis_response(message)
        return Response({'reply': reply}, status = status.HTTP_200_OK)
    except Exception:
        return Response({'error': 'Jarvis is temporarily unavaialable.'}, status = status.HTTP_503_SERVICE_UNAVAILABLE)
    
