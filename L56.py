import re
p = r"[:,-]"
str1 = "A:5, B:6, C:9-6"
print(str1, "->", re.sub(p, " ", str1), end=" ")