l = int(input("Enter the length "))
b = int(input("Enter the breadth "))
h = int(input("Enter the heigth "))
k = (l*l) + (b*b) + (h*h)
import math
v = ((b*b)*(h*h)) / math.sqrt(k)
print("volume of the tromboloid is ")
print('%0.3f'%v)
r = ((3/4)*v*(22/7))**(1/3)
print("radius of the sphere is ")
print('%0.3f'%r)
