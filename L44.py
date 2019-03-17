l1 = [0, 1, 2, 2, 3, 4, 5, 6, 4, 4, 2, 1]
print("Before removing duplicates:", l1)
l1 = list(dict.fromkeys(l1))
'''for i in l1:
    for j in range(l1.count(i)):
        l1.remove(i)'''
print("After removing duplicates:", l1)
