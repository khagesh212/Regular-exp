# Problem 2: Return the first two character of each word
# Solution-1 Extract consecutive two characters of each word, excluding
# spaces (using “\w“)

import re
k=input("Enter String:")
res= re.findall(r"\w\w",k)
print(res)
print("----------------------")

# Solution-2 Extract consecutive two characters those available at start
# of word boundary (using “\b“)

res=re.findall(r"\b\w.",k)
print(res)