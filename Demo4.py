# Example on re.split(pattern, string):
import re
N=input("Enter String:")
res=re.split(r"a",N)
print(res)
print("no of a's : ",(len(res)-1))