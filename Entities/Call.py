from datetime import datetime
from typing import List
from Entities.User import User

class Call:
    def __init__(self):
        self.call_id = None
        self.receivers: List[User] = []
        self.call_type = None
        self.started_at = None
        self.ended_at = None

    def set_call_type(self, type):
        self.call_type = type

    def start_time(self):
        self.started_at = datetime.now()

    def end_time(self):
        self.ended_at = datetime.now()

