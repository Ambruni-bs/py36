lst = []
lst = [int(item) for item in input("Enter 5 numbers : ").split()]
print("sliced list")
print(lst[:3])
lst[0] = 0
lst[4] = 0
lst1 = lst[:3]
lst1[0] = 0
lst1[2] = 0
print(lst)
print(lst1)
