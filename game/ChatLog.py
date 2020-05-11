from ChatMessage import ChatMessage


class ChatLog:
    def __init__(self, name):
        self.history = []
        self.name = name

    def add_message(self, who, what):
        self.history.append(ChatMessage(who, what))

    def delete_history(self):
        self.history = []
