# Example to validate Name
import re
user_name = input("Name Please :")
result = re.match("^[A-Za-z]*$", user_name)
if result == None:
    print("Invalid Name")
else:
    print("Welcome Mr/Miss : ",user_name)