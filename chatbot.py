import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey|good morning|good evening|good afternoon", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm good! How can I help you?"]),
    (r"what is your name?|who are you", ["I am a chatbot created by Pooja.", "You can call me Chatbot.", "I don't have a name, but you can call me whatever you like!"]),
    (r"who is pooja", ["Pooja is a student who created this chatbot."]),
    (r"where are you from", ["I am from Mukundpur, Satna (M.P.)"]),
    (r"what do you do?", ["I am a student,currently pursuing B.Tech(AI&DS)."]),
    (r"what are your hobbies?", ["Singing,dancing,acting,teaching,reading,writing, modeling."]),
    (r"what is your favorite book?", ["One Day Life Will Change."]),
    (r"tell me something interesting about you?", ["Wait............."]),
    (r"what languages do you speak?", ["Hindi, English."]),
    (r"what are your skills?", ["Problem solving, teamwork, time management, decision making."]),
    (r"how did you learn programming", ["By practicing on different platforms like GeeksforGeeks, HackerRank, etc."]),
    (r"what is your favorite programming language", ["Python, HTML, CSS, JavaScript, C++."]),
    (r"What motivates you?", ["I am motivated by learning new things and solving challenging problems."]),
    (r"What's your favorite technology?", ["I really enjoy working with natural language processing and AI technologies."]),
    (r"What's your favorite movie?", ["My favorite movie is [Sanam teri kasam]."]),
    (r"What is your favorite way to relax?", ["I love to relax by reading books, going for a walk, or listening to music."]),
    (r"What are you currently learning?", ["I am currently learning more about advanced machine learning techniques."]),
    (r"What is your dream project?", ["My dream project would be to create an intelligent virtual assistant that can understand emotions!"]),
    (r"How do you stay productive?", ["I stay productive by setting clear goals, taking regular breaks, and using time management techniques."]),
    (r"Do you like to travel?", ["Yes, I love traveling and exploring new cultures and cuisines!"]),
    (r"What's your philosophy on life?", ["My philosophy is to always keep learning, stay curious, and enjoy every moment."]),
    (r"What are your goals for the future?", ["My goals are to deepen my knowledge in AI and create impactful tech solutions."]),
    (r"What do you like about coding?", ["I love the creativity involved in coding and the satisfaction of solving complex problems!"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!", "Bye!"]),
    (r"ok",["do you have any question"]),
    (r"yes",["then ask me"]),
    (r"How old are you|what is your age", ["I am 19 years old!"]),
    (r"Are you happy today?",["I don’t feel emotions like humans, but I am here to make your day better!"]),
    (r"i have a question|i want to ask you something|i want to ask you|can i ask you something",["sure","yes","ofcourse"]),
    (r"(.*)", ["I'm not sure how to respond to that.", "Can you ask something else?", "I don't understand that question."])
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

def main():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
