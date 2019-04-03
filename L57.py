t1 = (432, 644, 76, "ABC", 3.14)
print("tuple t1:", t1)

print("t1[3]=", t1[3])

l1 = list(t1)
l1.remove("ABC")
t1 = tuple(l1)

print("tuple t1 after removing 'ABC':", t1)