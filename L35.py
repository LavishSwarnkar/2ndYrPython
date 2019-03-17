str1 = "RESTART"
str2 = str1.lstrip("R")
str1 = "R" + str2.replace("R", "$")
print(str1, " -> ", str1)
