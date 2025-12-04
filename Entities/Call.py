from typing import List
from User import User

class Call:
    def __init__(self):
        self.call_id = None
        self.receivers: List[User] = []
        self.call_type = None
        self.started_at = None
        self.ended_at = None

