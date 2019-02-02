income = int(input("Enter your income: "))
amt = income - 150000
if(income<=150000):
    print("You don't have to pay any tax!")
elif(income>150000 and income<=300000):
    print("You have to pay 10% tax, i.e., Rs.",(amt * 10)/100)
elif(income>300000 and income<=500000):
    print("You have to pay 20% tax, i.e., Rs.",(amt * 20)/100)
else:
    print("You have to pay 30% tax, i.e., Rs.",(amt * 30)/100)

