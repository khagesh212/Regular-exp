# Example on re.search(pattern, string):
import re
k=input("Enter String:")
res=re.search(r"Khagesh",k)
print(res)
print("------------------------------")
# To print the matching string we’ll use method group()
print("Matched word:",res.group())
print("------------------------------")
# To print start position of matching pattern in the string.
print("Start:",res.start())
# To print end position of matching pattern in the string.
print("End:",res.end())