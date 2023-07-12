class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


    def walk(self):
        self.pet.play()
        return self
        


# implement __init__( first_name , last_name , treats , pet_food , pet )
        	
    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class pet:
    def __init__(self,name,type,tricks,health,energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
 
    def play(self):
        self.health += 20
        return self
    
    def sleep(self):
        self.health += 25
        return self
    
    def noise(self):
        print('Hello sir')

doggy = pet('jorge','labrador','jump',50,30)
Imed = Ninja('Imed','Balbouli',doggy,'Bone','meat')

Imed.walk()
print(doggy.health)
# doggy.play().sleep().noise()
# print(doggy.health)
