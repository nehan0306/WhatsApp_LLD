from typing import List
from Entities.Message import Message
from Entities.Chat import Chat
from Entities.User import User

class MessageService:
    def fetch_all_messages(self, chat: Chat) -> List[Message]:
        return chat.messages

    def forward_message(self, message: Message, chat: Chat, sender: User) -> Message:
        forwarded_message = Message()
        forwarded_message.message_content = message.message_content
        forwarded_message.sender = sender
        forwarded_message.receiver_chat = chat
        forwarded_message.forward_status()
        return forwarded_message

    def send_message(self, chat: Chat, message: Message):
        chat.messages.append(message)
        message.receiver_chat = chat

