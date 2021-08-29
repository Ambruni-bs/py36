import math
def input_number():
    val=input("Enter the length, breadth and height").split(" ")
    val=[float(i) for i in val]
    return val[0],val[1],val[2]


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
