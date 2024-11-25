import nltk
import random
import string  # To process standard Python strings

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections

# Define conversation pairs for the chatbot
pairs = [
    [r"hello|hi|hey", ["Hi there!", "Hello! How can I assist you?"]],
    [r"how are you?", ["I'm just a chatbot, but I'm doing well! How about you?"]],
    [r"what is your name?", ["I'm your friendly chatbot!", "You can call me ChatBot."]],
    [r"what can you do?", ["I can help you with basic queries and have simple conversations."]],
    [r"goodbye|bye", ["Goodbye! Have a great day!", "See you soon!"]],
    [r"(.*)", ["Sorry, I don't understand that. Can you rephrase?"]]
]

# Initialize the chatbot
def chatbot_poc():
    print("ChatBot: Hi! I'm here to chat. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot_poc()
