str1 = input("Enter a string: ")
print("Uppercase of string is", str1.upper())
print("Lowercase of string is", str1.lower())
print("Titlecase of string is", str1.title())
list1 = str1.split()
for i in range(0, len(list1)):
    list1[i] = list1[i].title()
print("CamelCase of string is", ''.join(list1))
