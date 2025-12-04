class SharedMedia:
    def __init__(self):
        self.media_id = None
        self.media_type = None
        self.media_url = None
        self.is_deleted = None

    def delete_media(self):
        self.is_deleted = True
