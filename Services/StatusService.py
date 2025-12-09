from datetime import datetime, timedelta
from Entities.Status import Status
from Entities.User import User

class StatusService:
    def add_status(self, user: User, status: Status):
        status.user = user
        status.set_sent_time()

    def remove_status(self, status: Status):
        if datetime.now() - status.sent_at > timedelta(hours=24):
            status.set_delete_time()

    def delete_status(self, status: Status):
        status.set_deleted()
        status.set_delete_time()