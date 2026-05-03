# DAY 2 EXERCISES - 3RD MAY 2026
# Topic : String and String Methods 

#Exercise 1 : Basic strings
name = "Meshiyat Rubab"
city = "Lahore"
goal = "AI ENGINEER"

#Exercise 2 : String methods
print(name.upper())
print(name.lower())
print(name.replace("Rubab", "Developer"))
print(len(name))
print(name.count("a"))

#Exercise 3 : String slicing
print(name[0])      #first letter
print(name[-1])     #last letter
print(name[0:7])    #first 7 letters
print(name[8:])     #from 8th letter onwards

#Exercise 4 : String checking
print(name.startswith("M"))
print(name.endswith("b"))
print(name.isupper())
print(name.islower())