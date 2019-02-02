x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if(x>y):
    if(x>z):
        print(x," is greatest among the 3")
    else:
        print(z," is greatest among the 3")
else:
    if(y>z):
        print(y," is greatest among the 3")
    else:
        print(z," is greatest among the 3")
