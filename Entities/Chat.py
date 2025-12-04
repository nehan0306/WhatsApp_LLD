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

    def mute_notification(self):
        self.is_muted = True

