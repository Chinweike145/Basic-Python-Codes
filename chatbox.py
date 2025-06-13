import random
import re

# Dictionary containing patterns and responses
responses = {
    r'hello|hi|hey': ['Hello!', 'Hi there!', 'Hey!', 'Hi! How can I help you?'],
    r'bye|goodbye': ['Goodbye!', 'See you later!', 'Bye!', 'Have a great day!'],
    r'how are you': ['I am doing well, thank you!', 'I\'m fine, how about you?', 'I\'m good, thanks!'],
    r'i\'m okay|fine thank you|i\'m good': ['That\'s nice to hear', 'Great,your welcome', 'Awesome'],
    r'(.*) what is your name': ['I am just a chatbot.', 'I don\'t have a name. You can call me Chatbot.'],
    r'I need your help' : ['Sure, I can help you. What do you need assistance with?'],
    r'Can you tell me about Marwadi University': ['MU is one of the best college in Rajkot,Gujarat.Marwadi University is one of the top University in Rajkot offering BE,MBA,BCA,MCA,BBA,MCA,B.com,D2D,B.Arch.'],
    r'when was it founded': ['It was established in 2016 by the Marwadi Education Foundation through the Gujarat Private Universities Amendment Act 2016'],
    r'(.*) thank you|thanks': ['You\'re welcome!', 'No problem!', 'Anytime!']
}

def generate_response(user_input):
    for pattern, responses_list in responses.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return random.choice(responses_list)
    return "I'm sorry, I don't understand that."

# Chat loop
print("ChatBot: Hello! Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye!")
        break

    response = generate_response(user_input)
    print("ChatBot:", response)
