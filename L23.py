n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of", n, "natural numbers is ", sum)
print("Average of", n, "natural numbers is ", sum / n)
