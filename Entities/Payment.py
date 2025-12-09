from Entities.User import User

class Payment:
    def __init__(self):
        self.transaction_id = None
        self.sender = User()
        self.receiver = User()
        self.amount_sent = None
        self.status = None
        self.timestamp = None

    def update_payment_status(self, status):
        self.status = status

