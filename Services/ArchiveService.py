from typing import List
from Entities.Chat import Chat

class Archives:
    def get_all_archives(self, chats: List[Chat]):
        archived_messages = []
        for chat in chats:
            if chat.is_archive:
                archived_messages.append(chat)
        return archived_messages

    def add_to_archives(self, chat: Chat):
        chat.is_archive = True

    def remove_from_archives(self, chat: Chat):
        chat.is_archive = False

