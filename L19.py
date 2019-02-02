n = int(input("Enter a number: "))
n_copy = n
res = 0
while(n!=0):
    res+=(n%10)**3
    n=n//10
if(n_copy==res):
    print(n_copy,"is Armstrong Number.")
else:
    print(n_copy,"is NOT a Armstrong Number.")

