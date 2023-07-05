from bank import Bank
from individual import Admin, User

def user_login(bank):
    email = input("Email: ")
    password = input("Password: ")
    user = bank.check_user(email, password)
    # print(user)
    if user:
        print("Successfully Logged in...")
        user_options(bank, user)
    else:
        print("Invalid credentials!")
        # initial_options(bank)
        return 

def admin_login(bank):
    email = input("Email: ")
    password = input("Password: ")
    admin = bank.check_admin(email, password)
    # print(admin)
    if admin:
        print("Successfully Logged in...")
        admin_options(bank, admin)
    else:
        print("Invalid credentials!")
        # initial_options(bank)
        return

def initial_options(bank):
    while(True):
        print("=================== Login Options ===================")
        print("Press 1: To login as User")
        print("Press 2: To login as Admin")
        print("Press 3: End")
        print("*** Please login as user or admin to get the options ")
        print("-----------------------------------------------------")

        op = input()
        try:
            op = int(op)
        except Exception as e:
            print(str(e))
        if op == 1:
            user_login(bank)
        elif op == 2:
            admin_login(bank)
        elif op == 3:
            print("Bank Service is being terminated...")
            return
            # exit()
        else:
            print("Wrong key!")

def user_options(bank, user):
    while(True):
        print("============== User Options ==============")
        print("Press 1: To create account")    
        print("Press 2: To deposit Money")    
        print("Press 3: To withdraw Money")    
        print("Press 4: To check available balance")    
        print("Press 5: To transfer amount to another account")    
        print("Press 6: To check transaction history")   
        print("Press 7: To take a loan from the bank")
        print("Press 8: To check user details")
        print("Press 0: Back")
        print("-----------------------------------------")

        op = input()
        op = int(op)
        if op == 1:
            email = input("Email: ")
            password = input("Password: ")
            try:
                user.create_account(bank, email, password)
                print("Account has been created successfully!")
            except Exception as e:
                print("Error:", str(e))
        elif op == 2:
            if len(user.accounts) > 0:
                amount = input("Deposit amount: ")
                amount = int(amount)
                acc_no = input("Account No: ")
                user.deposit(bank, amount, acc_no)
            else:
                print("User don't have any account! Please create an account first!")   
        elif op == 3:
            if len(user.accounts) > 0:
                amount = input("Withdraw amount: ")
                amount = int(amount)
                acc_no = input("Account No: ")
                user.withdraw(bank, amount, acc_no)
            else:
                print("User don't have any account! Please create an account first!")
        elif op == 4:
            if len(user.accounts) > 0:
                acc_no = input("Check balance from which account (Account No): ")
                user.check_balance(bank, acc_no)                
            else:
                print("User don't have any account! Please create an account first!")
        elif op == 5:
            if len(user.accounts) > 0:
                amount = input("Transfer amount: ")
                amount = int(amount)
                from_acc_no = input("Account No to Transfer from: ")
                to_acc_no = input("Account No to Transfer to : ")
                user.transfer(bank, from_acc_no, to_acc_no, amount)
            else:
                print("User don't have any account! Please create an account first!")
        elif op == 6:
            user.check_transaction_history()
        elif op == 7:
            if bank.can_give_loan():
                if len(user.accounts) > 0:
                    amount = input("Requested Loan amount: ")
                    amount = int(amount)
                    for_acc_no = input("For which Account No: ")
                    user.take_loan(bank, amount, for_acc_no)
                else:
                    print("User don't have any account! Please create an account first!")
            else:
                print("Sorry, currently loan is unavailable!")
        elif op == 0:
            return
            # exit()
        elif op == 8:
            user.user_details()
        else:
            print("Wrong key!")
def admin_options(bank, admin):
    """    =============== What Admin can do =================
    Can create an account
    Can check the total available balance of the bank.
    Can check the total loan amount.
    Can on or off the loan feature of the bank.
    """
    while True:
        print("============== Admin Options ==============")
        print("Press 1: To create an account")
        print("Press 2: To check the total available balance of the bank")
        print("Press 3: To check the total loan amount")
        print("Press 4: To on or off the loan feature of the bank")
        print("Press 5: To check bank details")
        print("Press 0: Back")
        print("-------------------------------------------")

        op = input()
        op = int(op)
        if op == 1:
            email = input("Email: ")
            password = input("Password: ")
            # user_exist = input("User already existing? (yes/no):")
            # if user_exist=='yes':
            #     user = Bank.check_user(email, password)
            #     admin.create_account(bank, email, password)
            # elif user_exist == 'no':
            #     user.create_account(bank, email, password)

            # else:
            #     print("Invalid input! Try again...")
            try:
                admin.create_account(bank, email, password)
                print("User and account with the same email and password have been created successfully!")
                # print(bank)
            except Exception as e:
                print("Error:", str(e))
            
        elif op == 2:
            print("Total available balance of the bank: ", admin.bank.balance)
        
        elif op == 3:
            print("Total loan amount: ", admin.bank.loan)
        
        elif op == 4:
            admin.loan_control(bank)

        elif op == 5:
            print(bank)
        
        elif op == 0:
            return

        else:
            print("Wrong key!")


bank = Bank("ubl", 100000)
# admin = Admin("admin@gmail.com", "123")
# user = User("user@gmail.com", "123")
admin = Admin("a", "123")
user = User("u", "123")
user2 = User("v", "123")

bank.add_admin(admin)
bank.add_user(user)
bank.add_user(user2)

initial_options(bank)




