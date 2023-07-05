# from Account import Account
class Bank:
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.__balance = balance
        self.accounts = {}
        self.users = {}
        self.__loan = 0
        self.__give_loan = True
        self.admin = None

    def can_give_loan(self):
        return self.__give_loan
    
    def set_loan_giving(self, yes_no):
        self.__give_loan = yes_no
    
    @property
    def balance(self):
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance += amount
        # self.__balance = self.__balance + amount

    
    def deposit(self, amount):
        self.__balance += amount 

    
    def withdraw(self, amount):
        self.__balance -= amount 
    
    def transfer(self, from_acc_no, to_acc_no, amount):
        from_account = None
        to_account = None
        # for account in self.accounts.values():
        #     if account.acc_no == from_acc_no:
        #         from_account = account
        #     elif account.acc_no == to_acc_no:
        #         to_account = account
        #     if from_account and to_account:
        #         break;
        
        
    
    def give_loan(self, amount):
        self.__balance -= amount 
        self.__loan += amount

    @property
    def loan(self):
        return self.__loan
        

    
    def add_account(self, account):
        if account.email in self.accounts.keys():
            raise Exception("Account already exists!")
        else:
            self.accounts[account.email] = account

    # @staticmethod
    # def create_account(name, email, balance=0):
    #     account = Account(name, email, balance)
    #     # accounts[]
    #     return account
    def add_user(self, user):    
        # print("User: ", user.email)    
        self.users[user.email] = user

    @property
    def has_user(self):
        if len(self.users)>0:
            return True
        else:
            return False
        
    @property
    def has_admin(self):
        if self.admin:
            return True
        else:
            return False
        
    
    def check_user(self, email, password):
        # print(len(self.users))
        for mail in self.users.keys():
            # print(type(self.users[email].password))
            # print(email == mail)
            # print("mail: ", mail)
            # print("email: ", email)
            if email == mail and self.users[email].password == password:
                return self.users[email]
        return None
    
    
    def check_admin(self, email, password):
        if self.admin.email == email and self.admin.password == password:
            return self.admin
        else:
            return None
        

    def add_admin(self, admin):
        self.admin = admin
        self.admin.bank = self

    def __repr__(self) -> str:
        print("=============== Bank Details ================")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Loan: {self.__loan}")
        print(f"Admin: {self.admin}")
        if self.accounts: 
            print("============= List of Accounts ==============")
            for account in self.accounts.values():
                print(f'id: {account.acc_no}\temail: {account.email}')
        else:
            print("No account has been created yet!")
        
        if self.users:
            print("============== List of Users ===============")
            for user in self.users.keys():
                print(f'{user}')
        else:
            print("No user has been created yet!")
        print("\n")
        return ''

