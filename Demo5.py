# Example on re.split(pattern, string, [maxsplit=0]):
import re
N=input("Enter String:")
res=re.split(r"a",N,maxsplit=3)
print(res)
print("no of splits : ",(len(res)-1))