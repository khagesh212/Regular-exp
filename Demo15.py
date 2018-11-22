# To search if an e-mail address is in a string:
import re
k=input("Enter an email in string:")
res = re.search('[^@]+@[^@]+\.[^@]+',k)
if res:
    print("String found.")
else:
    print("Nothing found.")