str1 = "A:5, B:6, C:9-6"
print(str1, "->", end=" ")
str1 = str1.replace(":", " ")
str1 = str1.replace(",", " ")
str1 = str1.replace("-", " ")
print(str1)
