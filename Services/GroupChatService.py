from Entities.GroupChat import GroupChat
from Entities.User import User
from Services.ChatService import ChatService

class GroupChatService(ChatService):
    def make_admin(self, group_chat: GroupChat, user: User):
        pass

    def add_memebers(self, group_chat: GroupChat, users: list):
        pass

    def remove_members(self, group_chat: GroupChat, users: list):
        pass

    def search_members(self, query: str):
        pass

    def group_voice_call(self, group_chat: GroupChat):
        pass

    def group_video_call(self, group_chat: GroupChat):
        pass

    def exit_group(self, group_chat: GroupChat, user: User):
        pass