"""
In javaScript 
for (var i =0 ; i<10;i++){
console.log(i)
}

"""

#in Python 

"""
range = function that returns a sequence of numbers 
start : inclusive has a default value of 0
stop: exclusive and required 
step : not required and default 1 can be + or - 
example :
    range (0,10)=> (0,1,2,3,4,5,6,7,8,9)
"""
# for i in range(0,10):
#     print(i)

# for i in range(10,0,-2):
#     print(i)
    # for j in range(0,i):
    #     print(j)


# for i in range(10):
#     print(i)




super_heroes = ["superman","batman","aquaman","jedi"]
# for i in range(0,len(super_heroes)):
#     print(super_heroes[i])

first_str ="hello world"
name ="Jhon"
age = 41
is_Admin = False

my_list = [1,2,3,4,5,"45",name,age,is_Admin,["yes","no",None]]

# for element in my_list:
#     print(element)

user ={
    'first_name' : name,
    'last_name' : "Smith",
    'age' : age,
    'is_admin' : False,
    'marks': [10,9.8,10],
    'friends':{'one':"Alex",'two':"Max"}
}

# print(user.items())

#item.keys

# for key in user.keys():
#     print(f"KEY {key} *** {user[key]}")
    
# print(user.items())

#item.values

for value in user.values():
    print(f"KEY {value} *** {user[value]}")

    print(user.items())
