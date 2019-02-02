x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter Operation (+,-,*,/,//,**): ")
if(op=='+'):
    print(x,op,y," = ",x+y)
elif(op=='-'):
    print(x,op,y," = ",x-y)
elif(op=='*'):
    print(x,op,y," = ",x*y)
elif(op=='/'):
    print(x,op,y," = ",x/y)
elif(op=='//'):
    print(x,op,y," = ",x//y)
elif(op=='**'):
    print(x,op,y," = ",x**y)
else:
    print("Wrong operator!")
