# Example on re.match(pattern, string):
import re
k=input("Enter String:")
res=re.match(r"Khagesh",k)
print(res)
print("------------------------------")
print("Matched word:",res.group()) # To print the matching string we’ll use method group()
print("------------------------------")
print("Start:",res.start())  # To print start position of matching pattern in the string.
print("End:",res.end())  # To print end position of matching pattern in the string.