# Problem 5: Return all words of a string those starts with vowel
# Solution-1 Return each words

import re
k=input("Enter String:")
res=re.findall(r"\w+",k)
print(res)
print("---------------------------")

# Solution-2 Return words starts with alphabets (using [])
res=re.findall(r"[aeiouAEIOU]\w+",k)
print(res)