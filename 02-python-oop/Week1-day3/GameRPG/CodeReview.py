class BankAccount:
    all_account= []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate =0.02, balance= 0): 
        self.int_rate = int_rate
        self.balance = balance
        # self.all_account.append()
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(f"You added {amount}$ to your account")
        return self
        
    #     # your code here
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"You withdrawed {amount}$ from your account")
        else :
            self.balance -= 5
            print("not enaugh founds, You are charged 5 dollars")

        return self
    


    #     # your code here
    def display_account_info(self):
        print(f"Your balance is {self.balance}\nYour intrest rate is {self.int_rate}")
    #     # your code here
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    #     # your code here

account_1 = BankAccount(0.02,100)
account_2 = BankAccount(0.04,200)
# account_1.int_rate =0.02
# account_2.int_rate =0.01
# account_2.balance =0
# account_1.balance =0


# print(account_1.balance)
# account_1.deposit(10).withdraw(20).display_account_info()
account_1.yield_interest()