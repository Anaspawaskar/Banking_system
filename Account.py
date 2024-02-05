"""
    Here we are creating a bank account and generating the account id
"""
import uuid


class Account:
    """
    Here we are creating a bank account and generating the account id
    """

    def __init__(
        self,
        name,
        initial_deposit,
    ):
        """
        constructor for account class
        """

        self.name = name
        self.initial_deposit = initial_deposit
        self.account_id = uuid.uuid4().int % (10**12)
        self.transaction_history = []

    def new(self):
        """new tympss"""

    def new1(self):
        """new tympss"""
