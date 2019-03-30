from functools import reduce
l1 = [32, 543, 32, 2132, 322, 7687]
largest = reduce(lambda x,y : x if x>y else y, l1)
print("max(", l1, ") =", largest)
