msg = input("Enter a string: ")
occ = {}
for i in msg:
    if i in occ:
        occ[i] += 1
    else:
        occ[i] = 1
print("Occurences:", occ)