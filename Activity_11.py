def input_number():
        a = int(input("Enter the first number: "))
	b = int(input("Enter the second number: "))
	return a, b
def add(n1, n2):
	return n1+n2

def display(n1, n2, Sum):
	print(f"{n1} + {n2} = {Sum}")


def main():
	a,b = input_number()
	summation = add(a, b)
	display(a, b, summation)
main()
