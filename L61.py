d1 = {"Dec":12, "Nov":11, "Oct":10}
print("d1:", d1)
d1['Sep']=8
print("after adding ['Sep']:8, d1 =", d1)
d1.update(Sep = 9)      #d1['Sep']=9
print("after updating ['Sep']:9, d1 =", d1)
del d1["Sep"]           #d1.pop("Sep")
print("after deleting ['Sep']:9, d1 =", d1)