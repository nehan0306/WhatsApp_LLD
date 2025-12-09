class User:
    def __init__(self):
        self.user_id = None
        self.user_name = None
        self.phone_number = None
        self.about = None
        self.profile_picture = None

    def change_username(self, new_username):
        self.user_name = new_username

    def set_profile_pic(self, pic_url):
        self.profile_picture = pic_url

    def set_about(self, about_message):
        self.about = about_message
