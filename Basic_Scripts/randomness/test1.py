item1 = input("Enter item1: \n")
item2 = input("Enter item2: \n")
item3 = input("Enter item3: \n")

itemlist = [item1, item2, item3]
numlist = [1, 3, 6, 7, 9 ,10]
boollist= [True, False, False, True]

choice = int(input("enter a number between 1 -> 3 for list apparence"))

if choice == 1: 
    print(itemlist)
elif choice == 2 : 
    print(numlist)
elif choice == 3 : 
    print(boollist)
else :
    print("enter a number between 1->3")
    pass

print(type(numlist))
print(type(item3))

