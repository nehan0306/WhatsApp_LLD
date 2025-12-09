from typing import List
from Entities.Message import Message
from Entities.SharedMedia import SharedMedia

class Chat:
    def __init__(self):
        self.chat_id = None
        self.messages: List[Message] = []
        self.shared_media: List[SharedMedia] = []
        self.is_muted = None
        self.is_archive = None
        self.is_favorite = None

    def set_muted(self):
        self.is_muted = True

    def set_archived(self):
        self.is_muted = True

    def set_favorite(self):
        self.is_favorite = True

    def add_message(self, message):
        self.messages.append(message)

    def add_media(self, media):
        self.shared_media.append(media)


