class ValidationService:
    def __init__(self):
        self.accepted_file_type = []
        self.about_max_length = None

    def validate_profile_pic_type(self, file_type):
        if file_type not in self.accepted_file_type:
            return False
        return True

    def validate_about_length(self, about):
        if len(about) > self.about_max_length:
            return False
        return True
