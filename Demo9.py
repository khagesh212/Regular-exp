# Problem 3: Return the domain type of given email-ids
# Solution-1 Extract all characters after “@”

import re
k=input("Enter Email:")
res=re.findall(r"@\w+",k)
print(res)
print("-------------------------")

# Above, you can see that “.com”, “.in” part is not extracted. To add it,
# we will go with below code.
res=re.findall(r"@\w+.\w+",k)
print(res)
print("-------------------------")

# Solution – 2 Extract only domain name using “( )”
res=re.findall(r"@\w+.(\w+)",k)
print(res)