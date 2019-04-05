d1 = {"C":"1.Cat", "B":"2.Ball", "A":"3.Apple"}
print("d1:", d1)
print("sorted by keys =", sorted(d1))
print("sorted in reverse order =", sorted(d1, reverse=True))
print("sorted by values =", sorted(d1.items(), key=lambda x: x[1]))
