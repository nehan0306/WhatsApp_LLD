from datetime import datetime
from typing import List
from Entities.Reaction import Reactions
from Entities.User import User
from Entities.Chat import Chat

class Message:
    def __init__(self):
        self.message_id = None
        self.sender = User()
        self.receiver_chat = Chat()
        self.message_content = None
        self.reactions: List[Reactions] = []
        self.is_deleted = None
        self.is_edited = None
        self.is_drafted = None
        self.is_forwarded = None
        self.timestamp = None

    def set_sent_time(self):
        self.timestamp = datetime.now()

    def delete_message(self):
        self.is_deleted = True

    def edit_message(self, new_message):
        self.message_content = new_message
        self.is_edited = True

    def add_reactions(self, reaction: Reactions):
        self.reactions.append(reaction)

    def move_from_drafts(self):
        self.is_drafted = False

    def forward_status(self):
        self.is_forwarded = True

