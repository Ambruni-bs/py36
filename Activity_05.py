lst = []
lst = [int(item) for item in input("Enter 5 numbers : ").split()]
sum = 0
for i in lst:
    sum = sum + int (i)
print("Sum of all the numbers = ",sum)
