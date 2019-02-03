x = int(input("Enter a number: "))
f = 0
for i in range(2,int(x**0.5)+1):
    if(x%i==0):
        f=1
        break
if(f==0):
    print(x, "is a Prime number")
else:
    print(x, "is a Composite number")
        

