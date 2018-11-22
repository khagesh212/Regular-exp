# Problem 4: Return date from given string
# Here we will use “\d” to extract digit.

import re
k=input("Enter Email:")
res=re.findall(r"\d",k)
print(res)