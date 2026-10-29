import ollama

def get_jarvis_response(message):

    response = ollama.chat(
        model = "jarvis:latest",
        messages = [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a friendly seat-booking assistant. "
                    "You help users check available seats, book a random "
                    "available seat, and cancel their current booking. "
                    "Keep replies short and friendly. "
                    "For unrelated requests, politely explain your purpose. "
                    "Never claim a booking or cancellation succeeded unless "
                    "the backend confirms it."
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
