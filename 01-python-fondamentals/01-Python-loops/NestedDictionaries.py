
# x = [ [5,2,3], [10,8,9] ]
# students = [
#  {'first_name': 'Michael', 'last_name' : 'Jordan'},
#  {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#  'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#  'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# --------1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]-----

# x[1][0]= 15
# print (x)
 
# #------- 2. Change the last_name of the first student from 'Jordan' to 'Bryant'------

# students[0]['last_name']= "Bryant"
# print (students)
# #------3. In the sports_directory, change 'Messi' to 'Andres' -----
# sports_directory['soccer'][0] = "andreas"
# print (sports_directory)

# -----4. Change the value 20 in z to 30

# z[0]['y']=30
# print(z)

#2. Iterate Through a List of Dictionaries

students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
 ]
    

# def iterateDictionary(students):
#     for student in range(0,4):
#         print(students[student]['first_name'])
#     for student in range(0,4):
#         print(students[student]['last_name'])

# print(iterateDictionary(students))




    
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

#3. Get Values From a List of Dictionaries

# def iterateDictionary2(key_name, some_list):
    # for i in range(0,len(students)):
    #  print(students[i][key_name])
    

# print(iterateDictionary2('first_name',students))


#4. Iterate Through a Dictionary with List Values

dojo = {
 'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
 



def printInfo(dojo,some_list):
 sum = (len(dojo[some_list]))
 print(f"{sum}:LOCATIONS")
 for i in range(0,sum-1):
  print(dojo[some_list][i])
(printInfo(dojo,'locations'))

