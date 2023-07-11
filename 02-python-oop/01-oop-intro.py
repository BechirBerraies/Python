# OOP : Object oriented Programming 

student_1 =["Jhon" ,"Mayer" , 40 , [9.8,10,10],25]# List 

student_1 ={
    'firstname': "Jhon" ,'Last_Name': "Mayer" , 'Age':40 ,'Fav number ': [9.8,10,10], 'mark':25
}
student_1 ={
    'firstname': "Jhon" ,'Last_Name': "Mayer" , 'Age':40 ,'Fav number ': [9.8,10,10], 'mark':25
}
student_1 ={
    'firstname': "Jhon" ,'Last_Name': "Mayer" , 'Age':40 ,'Fav number ': [9.8,10,10], 'mark':25
}

class Student:
    def __init__(self,first_name,last_name,age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        


john =Student("john","Mayer",40)
print("****",john,"******")
print(f"FN:{john.first_name}\nLN: {john.last_name}")