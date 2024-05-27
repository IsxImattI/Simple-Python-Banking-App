from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner, initial_deposit=0):
        if account_number in self.accounts:
            return "Account number already exists!"
        else:
            self.accounts[account_number] = Account(account_number, owner, initial_deposit)
            return f"Account created for {owner} with initial deposit {initial_deposit}"

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None