from Entities.User import User
from Services.ValidationService import ValidationService
from Services.GCSService import GCSService

class UserService:

    def update_profile_pic(self, user: User, file_bytes, file_type):
        if not ValidationService().validate_profile_pic_type(file_type):
            raise ValueError("File type not supported")

        pic_url = GCSService().upload_to_gcs(file_bytes, file_type)

        user.set_profile_pic(pic_url)

    def update_about(self, user: User, about):
        if not ValidationService().validate_about_length(about):
            raise ValueError("About is too long")

        user.set_about(about)


    def update_user_settings(self):
        pass