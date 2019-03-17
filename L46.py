list1 = list(range(0, 11))
print("list1:", list1)

for x in range(0, 11):
    if x % 2 == 0:
        list1.remove(x)

print("After removing even numbers:", list1)