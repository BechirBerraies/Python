class Username : 
        
 def __init__(self,first_name,last_name,Email,Age):

    self.first_name = first_name
    self.last_name = last_name
    self.Email = Email
    self.Age = Age  
    self.is_rewards_member = False
    self.gold_card_points = 0


 def DisplayInfo(self):
         print(f"Your first name is :{self.first_name}\nYour last name : {self.last_name}\nYour Email: {self.Email}\nYour Age is : {self.Age}\n you ar a member {self.is_rewards_member}\n and you have {self.gold_card_points}")
         return self
    
 def Enroll(self):
    self.is_rewards_member = True 
    self.gold_card_points += 200
    return self
 
 def SpendAmount(self,amount):
     self.gold_card_points -= amount
     return self
     

Norman = Username('Norman','lowman','Norman@gmail.com',22)
imed = Username('imed','bourguiba','imed@gmail.com',22)

Norman.Enroll().SpendAmount(50).DisplayInfo()
imed.Enroll().SpendAmount(80).DisplayInfo()