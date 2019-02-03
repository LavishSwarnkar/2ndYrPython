x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
odd=""
even=""
if(x%2==0):
        even = str(x)+","
        x+=1
for i in range(x,y+1,2):
	odd += str(i)+","
	even += str(i+1)+","
print("Odd numbers: ", odd)
print("Even numbers: ", even)
