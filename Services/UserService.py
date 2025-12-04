from Entities.User import User

class UserService:
    def change_username(self, user: User, new_username):
        user.user_name = new_username

    def set_profile_pic(self, user: User, pic_url):
        user.profile_picture = pic_url

    def update_about(self, user: User, about_message):
        user.about = about_message

    def update_user_settings(self):
        pass