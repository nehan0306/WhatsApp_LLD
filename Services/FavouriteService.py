from typing import List
from Entities.Chat import Chat


class Favourites:
    def get_all_favourites(self, chats: List[Chat]):
        favourite_messages = []
        for chat in chats:
            if chat.is_archive:
                favourite_messages.append(chat)
        return favourite_messages

    def add_to_favourites(self, chat: Chat):
        chat.is_favorite = True

    def remove_from_favourites(self, chat: Chat):
        chat.is_favorite = False

