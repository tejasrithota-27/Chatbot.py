import nltk
import re
import random
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data packages
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', 
     ['Hello! How can I assist you today?', 'Hi there! What can I do for you?', 'Hey! How can I help?']),

    (r'what is your name\??', 
     ['I am a chatbot created to assist you.', 'You can call me Chatbot.']),

    (r'how are you\??', 
     ['I am a bot, so always good!', 'Doing great, thanks for asking!']),

    (r'(.*)(help|support)(.*)', 
     ['Sure, I am here to help. Please tell me your problem.', 'How can I assist you today?']),

    (r'(.*) your favorite (movie|book|food)(.*)', 
     ['I do not have preferences like humans, but I like to help you!']),

    (r'(.*) (created|made) you(.*)', 
     ['I was created using Python and NLTK library for NLP capabilities.']),

    (r'(.*) weather(.*)', 
     ['I am unable to provide weather info right now, but you can check your local weather app.']),

    (r'quit|exit|bye', 
     ['Goodbye! Have a great day.', 'See you later!']),

    (r'(.*)', 
     ['Sorry, I did not understand that. Can you please rephrase?', 
      'I am not sure I follow. Can you explain differently?', 
      'Could you please elaborate on that?'])
]

def chatbot():
    print("Hello! I am your friendly chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(random.choice(['Goodbye! Have a great day.', 'See you later!']))
                break

            response = chat.respond(user_input)
            if response:
                print(response)
            else:
                print(random.choice(['Sorry, I did not understand that.', 'Could you please elaborate?']))

        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Goodbye!")
            break

if __name__ == "__main__":
    chatbot()
