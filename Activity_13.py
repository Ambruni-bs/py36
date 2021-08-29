n1 = int(input("Enter the start number: "))
n2 = int(input("Enter the end number: "))
  
for num in range(n1, n2 + 1):
    if num % 2 != 0:
        print(num)
