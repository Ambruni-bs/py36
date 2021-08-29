def greatest(a, b, c):
    if (a>=b) and (a>=c):
        return a
    elif (b>=c) and (b>=a):
        return b
    else:
        return c
def main():
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    c = int(input("Enter the third number "))
    big = greatest(a, b, c)
    print("%d is the greatest number among %d, %d and %d"%(big, a, b, c))
main()
