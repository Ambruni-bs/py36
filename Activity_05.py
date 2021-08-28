a = input("Enter a list element separated by space ")
list  = a.split()[:5]
sum = 0
for i in list:
    sum = sum + int (i)
print("Sum of all the numbers = ",sum)
