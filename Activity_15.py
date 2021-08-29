import math
def input_number():
   l = int(input("Enter the length "))
   b = int(input("Enter the breadth "))
   h = int(input("Enter the heigth "))
   return l,b,h

def volume(l,b,h):
    k = (l*l) + (b*b) + (h*h)
    v = ((b*b)*(h*h)) / math.sqrt(k)
    return v

def display(v):
    print("volume of the tromboloid ")
    print('%0.3f'%v)

def main():
    l,b,h = input_number()
    volume_tromboloid = volume(l,b,h)
    display(volume_tromboloid)
main()    
