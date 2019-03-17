list1 = [231, 34, 22, 42, 15]
print("list1:", list1)

print("34 in list1:", 34 in list1)

print("22 not in list1:", 34 not in list1, "\n")

l1 = [True, True, True, True]
print("all(", l1, ")=", all(l1))
l1 = [True, False, True, True]
print("all(", l1, ")=", all(l1))
l1 = [0, 1, 2, 3]
print("all(", l1, ")=", all(l1))
l1 = [0, 0, 0, 0]
print("all(", l1, ")=", all(l1))
l1 = [0, 0, 0, 1]
print("all(", l1, ")=", all(l1))
l1 = []
print("all(", l1, ")=", all(l1), "\n")

l1 = [True, True, True, True]
print("any(", l1, ")=", any(l1))
l1 = [True, False, True, True]
print("any(", l1, ")=", any(l1))
l1 = [0, 1, 2, 3]
print("any(", l1, ")=", any(l1))
l1 = [0, 0, 0, 0]
print("any(", l1, ")=", any(l1))
l1 = [0, 0, 0, 1]
print("any(", l1, ")=", any(l1))
l1 = []
print("any(", l1, ")=", any(l1), "\n")

print("list('Lavish'): ", list('Lavish'))