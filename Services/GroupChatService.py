from typing import List
from Entities.GroupChat import GroupChat
from Entities.User import User
from Services.ChatService import ChatService

class GroupChatService(ChatService):
    def make_admin(self, group_chat: GroupChat, user: User):
        group_chat.admin_list.append(user)

    def add_memebers(self, group_chat: GroupChat, users: List[User]):
        group_chat.user_list += users

    def remove_member(self, group_chat: GroupChat, user: User):
        if user in group_chat.user_list:
            group_chat.user_list.remove(user)
        if user in group_chat.admin_list:
            group_chat.admin_list.remove(user)

    def search_members(self, group_chat: GroupChat, query: str):
        pass

    def group_voice_call(self, group_chat: GroupChat):
        pass

    def group_video_call(self, group_chat: GroupChat):
        pass

    def exit_group(self, group_chat: GroupChat, user: User):
        pass