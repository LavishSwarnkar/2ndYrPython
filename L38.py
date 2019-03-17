str1 = input("Enter a string: ")
list1 = list(str1)
temp = list1[0]
list1[0] = list1[len(list1)-1]
list1[len(list1)-1] = temp
print(''.join(list1))
