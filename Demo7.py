# Problem 1: Return the first word of a given string
# Solution-1 Extract each character (using “\w“)
import re
k=input("Enter String:")
res= re.findall(r".",k)
print(res)
print(len(res))
print("---------------------------")

# Above, space is also extracted, now to avoid it use “\w” instead of “.“
res= re.findall(r"\w",k)
print(res)
print(len(res))
print("-----------------------------")

# Extract each word (using “*” or “+“)
res= re.findall(r"\w*",k)
print(res)
#
res= re.findall(r"\w+",k)
print(res)
print("-----------------------------")

# Extract each word (using “^“)
res= re.findall(r"^\w+",k)
print(res)
print("-----------------------------")

# If we will use “$” instead of “^”, it will return the word from the end of
# the string. Let’s look at it.
res= re.findall(r"\w+$",k)
print(res)


