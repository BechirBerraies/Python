class BankAccount:


    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
     self.int_rate = int_rate
     self.balance = balance
     
    
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

        # your code here
    def withdraw(self, amount):
       self.balance -= amount
       return self
       
        # your code here
    def display_account_info(self):
       print(f"Your intrest rate : {self.int_rate} Your Balance : {self.balance} And your intrest yield is : {self.balance*self.int_rate} ")
       return
      #   # your code here
    def yield_interest(self):
      print(self.balance*self.int_rate)      
      return self



# Mohammed = BankAccount(0.05,200)
# Imed = BankAccount(0.03,2000)
# Mohammed.deposit(10).deposit(20).deposit(50).withdraw(10).yield_interest()
# # Mohammed.display_account_info()
# Imed.deposit(20).deposit(50).withdraw(1000).withdraw(200).withdraw(70).withdraw(200)
# Imed.display_account_info()
# Mohammed.yield_interest()
# print(Mohammed.balance)



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=100)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    	# your code here

    def make_withdrawal(self,amount):
       self.account.balance -= amount
       return self
    
    def displayBalance(self):
       print(f"Your account Balance is {self.account.balance}")

user1= BankAccount()
user1 = User('Amine','Amine@gmail.com')
# user1.make_deposit(40)

user1.displayBalance()

