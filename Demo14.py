# Email validation regex
import re
input = input("Enter an input string:")
m = re.match('[^@]+@[^@]+\.[^@]+',input)
if m:
    print("True")
else:
    print("False")