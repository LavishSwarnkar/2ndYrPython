name = input("Enter file name:")
f1 = open(name, mode="r")
occ = {}
for c in f1.read():
    if c in occ:
        occ[c] += 1
    else:
        occ[c] = 1
print("Occurences =", occ)
