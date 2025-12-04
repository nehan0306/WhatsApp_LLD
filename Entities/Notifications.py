from Entities.Chat import Chat
from Entities.Message import Message
from Entities.User import User

class Notifications:
    def __init__(self):
        self.notification_id = None
        self.message = Message()
        self.chat = Chat()
        self.receiver = User()
        self.is_read = None
        self.timestamp = None

    def mark_as_read(self):
        self.is_read = True

