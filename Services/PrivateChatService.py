from Entities.PrivateChat import PrivateChat
from Entities.User import User
from Services.ChatService import ChatService

class PrivateChatService(ChatService):
    def block_user(self, user: User):
        pass

    def voice_call(self, private_chat: PrivateChat):
        pass

    def video_call(self, private_chat: PrivateChat):
        pass

    def whatsapp_pay(self, private_chat: PrivateChat, amount):
        pass