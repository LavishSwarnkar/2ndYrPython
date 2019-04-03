t1 = (432, 644, 76, 3.14)
print("tuple t1:", t1)

print("length =", len(t1))
print("max =", max(t1))
print("min =", min(t1))

t2 = (56, 33, 2, 55)
print("tuple t2:", t2)
t1 += t2
print("concatenating t1 with t2:", t1)

print("(1,2)*3 =", (1, 2) * 3)

print((1, 2, 3), "<", (1, 2, 6), "=", (1, 2, 3) < (1, 2, 6))
print((1, 2), "<", (1, 2, 6), "=", (1, 2) > (1, 2, 6))
print((5, 2), ">", (1, 2, 6), "=", (5, 2) < (1, 2, 6))
print((5, 2, 6), ">", (1, 2, 6), "=", (5, 2, 6) > (1, 2, 6))