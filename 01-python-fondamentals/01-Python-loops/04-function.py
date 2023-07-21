"""
function ? => set of instruction 
could take arguments 
Must return something even None 
"""

# function sayHi(){
#     console.log('HI')
# }

# def say_hi(name):
    # print(f"Hi {name}")
#     return None



# Invoke // call the function 

# say_hi("Alex")


# def multiply(a*b):
#     return a*b

# print(multiply(2,3))

# multiply(1,2,3,5,65,4)



# def multiply(*args):
#     print(f"Args : {args}")
#     result=1
#     for number in args :
#         result *=number
#     return result

# print(multiply(1,2,3,5,65,41,2,3,5,6))

def say_Fullname(**kwargs):
    # print(f"Your full name is : {first_name} {last_name}!")
    # return f"{first_name}{last_name}"

    print(f"KWARGS : {kwargs}")
    print(f"FIRST NAME : {kwargs['first_name']}\nLAST NAME : {kwargs['last_name']}")
    return None
say_Fullname(first_name= "BOB",last_name = "MARLEY")