Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pip install chatterbot


from chatterbot import ChatBot
chatbot = ChatBot("marta")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "¿Holiis cómo estás?",
    "¿Qué andas haciendo?",
    "Que lindo día para ver las estrellas",
    
   
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)


response = chatbot.get_response("Que lindo día para ver las estrellas!")
print(response)

