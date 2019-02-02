x = int(input("Enter initial number: "))
y = int(input("Enter final number: "))
x_sum = (x*(x+1))//2
y_sum = (y*(y+1))//2
print("Sum of numbers from", x, "to", y, "is", y_sum-x_sum+x)
#OR
'''
n_sum=0
for i in range(x,y+1):
    n_sum+=i
print("Sum of numbers from", x, "to", y, "is", n_sum)
'''


