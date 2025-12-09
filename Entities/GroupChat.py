from typing import List
from Entities.User import User
from Entities.Chat import Chat

class GroupChat(Chat):
    def __init__(self):
        super().__init__()
        self.group_name = None
        self.group_icon = None
        self.group_description = None
        self.user_list: List[User] = []
        self.admin_list: List[User] = []

    def set_group_name(self, group_name):
        self.group_name = group_name

    def set_group_icon(self, group_icon_url):
        self.group_icon = group_icon_url

    def set_group_description(self, group_description):
        self.group_description = group_description
