import uuid


class Account():
    def __init__(self, name, _initial_deposit):
        """constructor for account class"""
        self.name = name 
        self.initial_deposit = _initial_deposit
        self.account_id = uuid.uuid4(). int % (10**12)
        self.transaction_history = []
        

        
