from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
#training the chatbot
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
#getting response
response = chatbot.get_response("Good morning!")
print(response)
