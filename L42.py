list1 = [231, 34, 22, 42, 15]
print("list1:", list1)

list1.insert(0, 99)
print("After inserting 99 at index 0:", list1)

list1.pop(3)
print("After pop at index 3:", list1)

list1.remove(42)
print("After removing 22:", list1)

list2 = [32, 24, 5454, 32]
print("list2:", list2)

list1.extend(list2)

print("Extending list1 with list2:", list1)