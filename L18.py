a = int(input("Enter marks in English (/100): "))
b = int(input("Enter marks in Maths (/100): "))
c = int(input("Enter marks in Science (/100): "))
d = int(input("Enter marks in Social Science (/100): "))
agg = (a+b+c+d)/4
if(agg >= 75):
    print("You have distinction.")
elif(agg>=60 and agg<75):
    print("You are PASS with I division.")
elif(agg>=50 and agg<60):
    print("You are PASS with II division.")
elif(agg>=40 and agg<50):
    print("You are PASS with III division.")
else:
    print("You are FAIL!")
