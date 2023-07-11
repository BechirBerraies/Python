# def firstletters(e):
#   result = ""
#   dog =  (e.split())
#   for i in range(0,len(dog)):
#     result += dog[i][0].upper()
#   print(result)
   





def split(e): 
  results=""
  for i in range(0,len(e)):
    if(e[i] == " "):
      results +=(e[i+1]).upper()
  print(results)


split(" object oriented programming")


"""
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without


"""

# const str1 = "object oriented programming";
# const expected1 = "OOP";

# # The 4 pillars of OOP
# const str2 = "abstraction polymorphism inheritance encapsulation";
# const expected2 = "APIE";

# const str3 = "software development life cycle";
# const expected3 = "SDLC";

# # Bonus: ignore extra spaces
# const str4 = "  global   information tracker    ";
# const expected4 = "GIT";

# function acronymize(str) {}