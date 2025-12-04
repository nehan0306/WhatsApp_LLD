from Entities.Chat import Chat

class GroupChat(Chat):
    def __init__(self):
        super().__init__()
        self.group_name = None
        self.group_icon = None
        self.group_description = None
        self.user_list = []
        self.admin_list = []