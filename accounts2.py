"""
    Accounts.py
"""

class Accounts:
    def __init__(self, account_number, account_firstname, account_lastname, current_balance, address,email):
      
        self.account_number = account_number
        self.account_firstname = account_firstname
        self.account_lastnmae = account_lastname
        self.current_balance = current_balance
        self.address = address
        self.email = email
    
    def update_address(self, new_address):
        self.Address = new_address
        
    def update_email(self, new_email):
        self.email = new_email
