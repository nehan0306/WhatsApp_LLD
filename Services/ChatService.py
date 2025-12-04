from datetime import datetime
from Entities.Chat import Chat
from Entities.Message import Message
from Entities.SharedMedia import SharedMedia
from Entities.User import User


class ChatService:
    def send_message(self, user: User, chat: Chat, message: Message):
        chat.messages.append(message)
        message.sender = user
        message.receiver_chat = chat
        message.timestamp = datetime.now()

    def send_voice_message(self, chat: Chat, message: Message, voice_message_url):
        message.message_content = voice_message_url
        chat.messages.append(message)
        message.receiver_chat = chat
        message.timestamp = datetime.now()

    def add_attachments(self, chat: Chat, media: SharedMedia):
        chat.shared_media.append(media)

    def search_message(self, chat: Chat, search_word: str):
        found_messages = []
        for message in chat.messages:
            if search_word.lower() in message.message_content.lower():
                found_messages.append(message)
        return found_messages


