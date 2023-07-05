from bank import Bank
from Account import Account
from abc import ABC, abstractmethod
from transaction import Transaction


class Individual(ABC):
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    @abstractmethod
    def create_account(self, bank, email, password):
        if email in bank.accounts.keys():
            raise Exception("Account with the same email already exists!")
        else:
            account = Account.create_account(bank, email, password)
            bank.add_account(account)
            # print(bank)
            # print("Account has been created successfully!")
            # print(account)
            return account
        

class User(Individual):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.accounts = {}
        self.transactions = []

    def create_account(self, bank, email, password):
        account = super().create_account(bank, email, password)
        # self.account = account
        self.accounts[account.email] = account
    
    def add_account(self, bank, account):
        self.accounts[account.email] = account
        bank.accounts[account.email] = account
    
    def deposit(self, bank, amount, acc_no):        
        deposited = False
        for item in self.accounts.values():
            # print(item)
            if item.acc_no == acc_no:
                bank.accounts[item.email].balance += amount
                bank.deposit(amount)
                self.accounts[item.email] = bank.accounts[item.email]
                deposited = True
        if deposited:
            print("Successfully deposited ", amount, " in your account")
            transaction = Transaction(f"Successfully deposited {amount} in account {acc_no} by {self.email}", acc_no)
        else:
            print("User have no such account!")
            transaction = Transaction(f"Failed to deposit {amount} in account {acc_no} by {self.email}", acc_no)
        self.transactions.append(transaction)
         

    def withdraw(self, bank, amount, acc_no):
        # User can only withdraw and transfer money from his account if he has money in his account.
        # If a user is unable to withdraw the amount of money he has deposited in the bank,
        # he will get a message that the bank is bankrupt.
        withdrawn = False
        for item in self.accounts.values():
            if item.acc_no == acc_no:
                if self.accounts[item.email].balance >= amount and bank.get_balance() >= amount:
                    bank.accounts[item.email].balance -= amount        
                    bank.withdraw(amount)
                    self.accounts[item.email] = bank.accounts[item.email]                    
                    withdrawn = True
                elif self.accounts[item.email].balance >= amount and bank.get_balance() < amount:
                    print("The bank is bankrupt!")
                elif  self.accounts[item.email].balance < amount:
                    print("You don't have enough money in your account!")
        
        if withdrawn:
            print("Successfully withdrawn ", amount, " from your account ", acc_no)
            transaction = Transaction(f"Successfully withdrawn {amount} from account {acc_no} by {self.email}", acc_no)
        else:
            print("User have no such account!")
            transaction = Transaction(f"Failed to deposit {amount} in account {acc_no} by {self.email}", acc_no)
        self.transactions.append(transaction)

    def check_balance(self, bank, acc_no):
        checked = False
        for item in bank.accounts.values():
            # print(item)
            if item.acc_no == acc_no:
                print("Current Account Balance: ", bank.accounts[item.email].balance)
                # print(self.accounts[item.email])
                checked = True
        if not checked:
            print("User have no such account!")   
        # if len(self.accounts) > 0:
        #     checked = False
        #     acc_no = input("Check balance from which account (Account No): ")
        #     for item in bank.accounts.values():
        #         # print(item)
        #         if item.acc_no == acc_no:
        #             print("Current Account Balance: ", bank.accounts[item.email].balance)
        #             # print(self.accounts[item.email])
        #             checked = True
        #     if not checked:
        #         print("User have no such account!")  
        # else:
        #     print("User don't have any account!") 
    

    def transfer(self, bank, from_acc_no, to_acc_no, amount):
        # User can only withdraw and transfer money from his account if he has money in his account.
        # for item in self.accounts.values():
        #     if item.acc_no == from_acc_no:                
        transferred = False
        from_account = None
        to_account = None
        for account in self.accounts.values():
            if account.acc_no == from_acc_no:
                from_account = account
                break;
        for account in bank.accounts.values():
            if account.acc_no == to_acc_no:
                to_account = account
                break;
        if from_account and to_account:
            if from_account.balance >= amount and bank.get_balance() >= amount:
                    bank.accounts[from_account.email].balance -= amount        
                    bank.accounts[to_account.email].balance += amount        
                    self.accounts[from_account.email] = bank.accounts[from_account.email]
                    self.accounts[to_account.email] = bank.accounts[to_account.email]                    
                    print(f"Successfully Transferred {amount} from account {from_acc_no} to account {to_acc_no}")
                    transaction = Transaction(f"Successfully Transferred {amount} from account {from_acc_no} to account {to_acc_no} by {from_account.email}", from_acc_no)
                    transferred = True
            elif from_account.balance >= amount and bank.get_balance() < amount:
                print("The bank is bankrupt!")
            elif  self.accounts[from_account.email].balance < amount:
                print("You don't have enough money in your account!")
            # bank.transfer(from_acc_no, to_acc_no, amount)
        elif not from_account and to_account:
            print(f"Account {from_account} doesn't exist!")
        elif from_account and not to_account:
            print(f"Account {to_account} doesn't exist!")
        else:
            print("Sorry, transfer is not possible!")

        if not transferred:
            transaction = Transaction(f"Failed to transfer {amount} from account {from_acc_no} to account {to_acc_no} by {from_account.email}", from_acc_no)
        self.transactions.append(transaction)
        
    def check_transaction_history(self):
        if len(self.transactions):
            print("============== Transaction History ==============")
            for each in self.transactions:
                print(each)
        else:
            print("No transaction has been done yet!")
        print("\n")

    def take_loan(self, bank, amount, for_acc_no):
        if len(self.accounts) > 0:
            if bank.can_give_loan():
                took_loan = False
                for item in self.accounts.values():
                    if item.acc_no == for_acc_no:
                        if self.accounts[item.email].balance*2 >= amount and bank.get_balance() >= amount:
                            bank.accounts[item.email].loan += amount        
                            bank.give_loan(amount)
                            self.accounts[item.email] = bank.accounts[item.email]
                            print("Loan of ", amount, " has been sanctioned successfully for your account ", for_acc_no)
                            transaction = Transaction(f"Loan of {amount} has been sanctioned successfully for your account {for_acc_no} by {self.email}", for_acc_no)
                            took_loan = True
                        # elif self.accounts[item.email].balance*2 < amount or bank.get_balance() < amount:
                        #     print("Loan sanction has been denied!")
                        # else:
                        #     print("Loan sanction has been denied!")
                if not took_loan:
                    print("Loan sanction has been denied!")
                    transaction = Transaction(f"Loan sanction of {amount} failed for account {for_acc_no} by {self.email}", for_acc_no)
                self.transactions.append(transaction)
            else:
                print("Sorry, currently loan is unavailable!")
        else:
            print("User don't have any account!")

    def user_details(self):
        print(f"=============== User Details ================")
        print(f"Email: {self.email}")
        # print(self.accounts)
        if self.accounts: 
            print("============= List of Accounts ==============")
            for account in self.accounts.values():
                print(f'Account No: {account.acc_no}\tEmail: {account.email}\tBalance: {account.balance}\tLoan: {account.loan}')
        else:
            print("No account has been created yet!")
        print("\n")
        return ''        

    def __repr__(self) -> str:
        return f'{self.email}\t{self.password}\n'

class Admin(Individual):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.bank = None
    
    def create_account(self, bank, email, password):
        account = super().create_account(bank, email, password)
        # print(f'Account No: {account.acc_no}')
        user = bank.check_user(email, password)
        if not user:
            user = User(email, password)            
        # print("User: ", user)
        user.add_account(bank, account)
        bank.add_user(user)
    
    def check_bank_balance(self):
        pass
    def check_total_loan_amount(self):
        pass
    def loan_control(self, bank):
        sanction = input("On or Off Loan Sanction (on/off):")
        if sanction == 'on':
            bank.set_loan_giving(True)
            print("Successfully turned on loan giving option.")
            return
        elif sanction == 'off':
            bank.set_loan_giving(False)
            print("Successfully turned off loan giving option.")
            return
        else:
            print("Wrong input!")
    def __repr__(self) -> str:
        # return f'{self.email}\t{self.bank}'
        return f'{self.email}\n'
    

