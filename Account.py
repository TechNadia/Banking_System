from bank import Bank
# import datetime
class Account:
    def __init__(self, bank, email, password) -> None:
        self.email = email
        self.password = password
        self.acc_no = str(len(bank.accounts) + 1)
        print("Account No is: ", self.acc_no)
        self.__balance = 0
        self.__loan = 0

    @staticmethod   
    def create_account(bank, email, password):
        if email in bank.accounts.keys():
            raise Exception("Account with the same email already exists!")
        else:
            account = Account(bank, email, password)
            # bank.add
            return account
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @property
    def loan(self):
        return self.__loan
    
    @loan.setter
    def loan(self, amount):
        self.__loan = amount
        
    def __repr__(self) -> str:
        return f'Account No: {self.acc_no}\temail: {self.email}\tbalance: {self.__balance}\tloan: {self.loan}\n'