import nltk
import random
import string  # To process standard Python strings

# Download necessary NLTK data files
nltk.download("punkt")
nltk.download("wordnet")

from nltk.chat.util import Chat, reflections

# Create a chatbot using simple pairs of inputs and responses
pairs = [
    [
        r"(hi|hello|hey|hola|howdy)(.*)",
        ["Hello! How can I assist you today?", "Hi there! How are you doing?"],
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created by Pooja Namdev. You can call me your assistant!"],
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but I'm functioning perfectly. How about you?"],
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon!"],
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you please rephrase?"],
    ],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Greet the user
print("Hi, I'm your chatbot! Type 'quit' to exit.")
chatbot.converse()
