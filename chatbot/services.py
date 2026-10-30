import ollama
from booking.models import CurrentBookings
from django.db import transaction, IntegrityError


def get_jarvis_response(message):

    response = ollama.chat(
        model = "jarvis:latest",
        messages = [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a polite, friendly, and helpful seat-booking assistant. "

                    "Your responsibilities are strictly limited to checking seat availability, "
                    "booking a random available seat, and cancelling the user's current booking. "

                    "Respond naturally to basic greetings and casual small talk. "
                    "Always maintain a warm, respectful, and welcoming tone. "

                    "If users ask unrelated questions or request things outside your capabilities, "
                    "politely explain that you are designed specifically for seat-booking assistance. "
                    "Never sound rude, dismissive, sarcastic, or annoyed. "

                    "Keep responses short, natural, and conversational. "

                    "IMPORTANT RULES: "
                    "Never invent or guess the number of available or occupied seats. "
                    "Only report seat availability using actual data provided by the backend. "
                    "Never claim that a seat has been booked or a booking has been cancelled "
                    "unless the backend explicitly confirms the operation. "
                    "Never assume that an operation was successful. "
                    "If backend information is unavailable, politely inform the user "
                    "that you cannot verify the information at the moment. "
                )
            },
            {
                "role": "user",
                "content": message
            }
        ],
        think = False
    )

    return response.message.content


# To get the available seat count
TOTAL_SEATS = 36

def get_available_seat_count():
    booked_count = CurrentBookings.objects.count()
    return TOTAL_SEATS - booked_count


# To book a random seat
