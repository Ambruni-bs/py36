a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = a + b
print(str(a) + ' + ' + str(b) + ' = ' + str(c))

#other ways to do formatting before printing

print(a,end=' + ')
print(b,end=' = ')
print(c)

print( '{x}  +  {y}  = {z}' .format(x=a,y=b,z=c))
