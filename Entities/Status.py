from datetime import datetime
from typing import List

from Entities.User import User

class Status:
    def __init__(self):
        self.user = User()
        self.status_type = None
        self.status_content = None
        self.sent_at = None
        self.seen_by: List[User] = []
        self.is_deleted = True
        self.deleted_at = None

    def set_sent_time(self):
        self.sent_at = datetime.now()

    def set_deleted(self):
        self.is_deleted = True

    def set_delete_time(self):
        self.deleted_at = datetime.now()

