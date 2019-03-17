def list_search(l, x):
    occ = []

    for i in range(0, len(l)):
        if l[i] == x:
            occ.append(i)

    return len(occ), occ


l1 = [0, 1, 2, 2, 3, 4, 5, 6, 4, 4, 2, 1]
print("list:", l1)

x = int(input("Enter number to be searched: "))

i, occ = list_search(l1, x)
if i > 0:
    print(x, "found at indices", occ)
else:
    print(x, "not found!")
