from Entities.Chat import Chat
from Entities.User import User

class PrivateChat(Chat):
    def __init__(self):
        super().__init__()
        self.user1: User
        self.user2 = User()
        self.is_blocked = None
        self.mute_duration = None

    def block(self):
        self.is_blocked = True
